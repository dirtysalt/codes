#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import defaultdict

import pymongo
from bs4 import BeautifulSoup

client = pymongo.MongoClient()
table = client.playfm.cache


def get_featured_items():
    rs = table.find()
    for r in rs:
        url = r['_id']
        if url.startswith('https://player.fm/mu/featured/'):
            yield r


def get_featured_tags():
    def pred(x):
        if not hasattr(x, 'attrs'): return False
        return x.attrs.get('data-toggle', '') == 'popover'

    def parse_single_page(data):
        d = {}
        bs = BeautifulSoup(data)
        tops = [x for x in bs.findAll('a') if pred(x)]
        for t in tops:
            text = t.text
            d[text] = []
            if 'data-content' not in t.attrs:
                continue
            sub_bs = BeautifulSoup(t.attrs['data-content'])
            subs = [x.text for x in sub_bs.select('a')]
            d[text] = subs
        return d

    tags = defaultdict(list)
    for r in get_featured_items():
        print('handling url = {}'.format(r['_id']))
        data = r['data']
        d = parse_single_page(data)
        for k in d:
            tags[k].extend(d[k])
    return tags


if __name__ == '__main__':
    tags = get_featured_tags()
    print(tags)
