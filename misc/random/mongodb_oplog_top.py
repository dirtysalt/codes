#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
分析Mongodb oplog, 对所有的操作做groupby. 看哪种操作数量比较多
"""

import time
from collections import Counter

import argparse
import bson
import pymongo
from collections import defaultdict

def list_keys(d, keys, prefix):
    for k, v in d.items():
        if isinstance(v, dict):
            k2 = prefix + k + '.'
            list_keys(v, keys, k2)
        else:
            k2 = prefix + k
            keys.append(k2)


def run(url, ts, refresh_interval, to_ts):
    ts = bson.Timestamp(int(ts), 0)
    init_dt = ts.as_datetime()
    print('ready to fetch oplogs. from_date = {}, refresh_interval = {}'.format(ts.as_datetime(), refresh_interval))
    src_client = pymongo.MongoClient(url)
    oplog = src_client.local.oplog.rs

    counter = Counter()
    last = time.time()
    rec_cnt = 0
    delta = defaultdict(int)

    while True:
        query = {'ts': {'$gt': ts}}

        # For a regular capped collection CursorType.TAILABLE_AWAIT is the
        # only option required to create a tailable cursor. When querying the
        # oplog the oplog_replay option enables an optimization to quickly
        # find the 'ts' value we're looking for. The oplog_replay option
        # can only be used when querying the oplog.
        cursor = oplog.find(query,
                            cursor_type=pymongo.CursorType.TAILABLE_AWAIT,
                            oplog_replay=True)
        while cursor.alive:
            for doc in cursor:
                ns = doc['ns']
                ts: bson.Timestamp = doc['ts']
                keys = []
                if 'o' in doc:
                    d = doc['o']
                    list_keys(d, keys, ns + '.')
                for k in keys:
                    delta[k] += 1

                rec_cnt += 1
                now = time.time()
                if (now - last) > refresh_interval:
                    counter.update(delta)
                    tops = counter.most_common(20)
                    now_dt = ts.as_datetime()
                    delta_secs = (now_dt - init_dt).total_seconds()
                    print('===== {} / {:.2f} hours, # of docs = {} ====='.format(ts.as_datetime(), delta_secs / 3600, rec_cnt))
                    max_key_len = max((len(x[0]) for x in tops))
                    fmt = '%-{}s    %-10d(+%d)'.format(max_key_len)
                    for k, v in tops:
                        print(fmt % (k, v, delta[k]))
                    print('\n\n')
                    last = now
                    delta.clear()

                if now > to_ts:
                    break

            # We end up here if the find() returned no documents or if the
            # tailable cursor timed out (no new documents were added to the
            # collection for more than 1 second).
            time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ago-hours', action='store', type=float, default=0.5)
    parser.add_argument('--refresh-seconds', action='store', type=int, default=10)
    parser.add_argument('--duration-hours', action='store', type=float, default = 24.0)
    parser.add_argument('--url', action='store')
    args = parser.parse_args()
    now = int(time.time())
    ago_hours = args.ago_hours
    dur_hours = args.duration_hours
    url = args.url
    refresh_seconds = args.refresh_seconds
    run(url, now - ago_hours * 3600, refresh_seconds, now - ago_hours * 3600 + dur_hours * 3600)
