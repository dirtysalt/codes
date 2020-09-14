#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
在两个mongodb集群之间同步所有DB之间的数据
"""

from __future__ import print_function

import time
from collections import defaultdict

import argparse
import bson
import os
import pymongo
import pymongo.errors


def flush_buffers(table, buffers, ordered, dry_run):
    if not buffers:
        return

    if dry_run:
        for x in buffers:
            print(x)
        return

    def fmt(x):
        if x['op'] == 'i':
            op = x['o']
            return pymongo.UpdateOne({'_id': op['_id']}, {'$set': op}, upsert=True)
        elif x['op'] == 'u':
            return pymongo.UpdateOne(x['o2'], x['o'], upsert=True)
        elif x['op'] == 'd':
            return pymongo.DeleteMany(x['o'])

    ops = [fmt(x) for x in buffers]
    print('update {} records'.format(len(ops)))

    try:
        table.bulk_write(ops, ordered=ordered)
    except pymongo.errors.BulkWriteError as e:
        print(e.details)


def load_ckpt(ckpt_path):
    if not os.path.exists(ckpt_path):
        return None
    with open(ckpt_path) as fh:
        ts = int(fh.read().strip())
    return ts


def write_ckpt(ckpt_path, ts):
    print('sync ts = {}'.format(ts.time))
    with open(ckpt_path, 'w') as fh:
        fh.write("{}\n".format(ts.time))


# http://api.mongodb.com/python/current/examples/tailable.html?highlight=tailed%20cursor


def flush_buffers_dict(dst_client, buffers_dict, ordered, dry_run):
    for ns in buffers_dict:
        if ns.startswith('admin') or ns.startswith('local'):
            buffers_dict[ns].clear()
            continue

        db, tbl = ns.split('.')
        table = dst_client[db][tbl]
        flush_buffers(table, buffers_dict[ns], ordered, dry_run)
        buffers_dict[ns].clear()


def sync(args):
    last_ts = load_ckpt(args.ckpt)
    ts = last_ts if last_ts is not None else int(args.ts)
    ts = bson.Timestamp(ts, 0)

    src_client = pymongo.MongoClient(args.src_url)
    oplog = src_client.local.oplog.rs
    dst_client = pymongo.MongoClient(args.dst_url)

    buffers_dict = defaultdict(list)
    while True:
        # For a regular capped collection CursorType.TAILABLE_AWAIT is the
        # only option required to create a tailable cursor. When querying the
        # oplog the oplog_replay option enables an optimization to quickly
        # find the 'ts' value we're looking for. The oplog_replay option
        # can only be used when querying the oplog.
        cursor = oplog.find({'ts': {'$gt': ts}},
                            cursor_type=pymongo.CursorType.TAILABLE_AWAIT,
                            oplog_replay=True)
        while cursor.alive:
            for doc in cursor:
                ts = doc['ts']
                ns = doc['ns']
                buffers_dict[ns].append(doc)

            # We end up here if the find() returned no documents or if the
            # tailable cursor timed out (no new documents were added to the
            # collection for more than 1 second).
            time.sleep(5)
            flush_buffers_dict(dst_client, buffers_dict, args.ordered, args.dry_run)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sync', action='store_true')
    parser.add_argument('--src-url')
    parser.add_argument('--dst-url')
    parser.add_argument('--ts')
    parser.add_argument('--bufsize', default=20, type=int)
    parser.add_argument('--ordered', default=False, type=bool)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--ckpt', default='syncer.ckpt')
    args = parser.parse_args()

    if args.sync:
        sync(args)


if __name__ == '__main__':
    main()
