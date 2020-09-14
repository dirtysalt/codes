#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict

import argparse
import hashlib
import json
import pandas
import pymongo
import re
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient()
db = client['stitcher']
cache_table = db['cache']


def get_cache_data(key):
    r = cache_table.find_one({'_id': key}) or {}
    return r.get('data')


def set_cache_data(key, data):
    cache_table.update_one({'_id': key}, {'$set': {'data': data}}, upsert=True)


def ensure_bytes(s, encoding='utf8'):
    if isinstance(s, str):
        return s.encode(encoding)
    return s


def get_sha1_key(s):
    s = ensure_bytes(s)
    return hashlib.sha1(s).hexdigest()


def request_url_by_cache(url):
    key = get_sha1_key(url)
    data = get_cache_data(key)
    if data is None:
        resp = requests.get(url)
        data = resp.content
        set_cache_data(key, data)
    return data


regexp = re.compile(r"""window.location.href='([^']+)'""")


def search_stitcher(name):
    uid = 123
    url = 'https://www.stitcher.com/Service/Search.php?uid={uid}&term={query}&s=0&c=10&searchType=feed&src=keyword&from=site&topHitsBy=relevance&mode=website'.format(
        uid=uid, query=name)
    data = request_url_by_cache(url)
    bs = BeautifulSoup(data, "lxml")
    feeds = bs.select('search > feed')
    if not feeds: return
    feed = None
    for f in feeds:
        if f.attrs['name'] == name:
            feed = f
            break
    feed = feed or feeds[0]
    seo_key = feed.attrs['seokey']
    url = 'https://www.stitcher.com/podcast/{}'.format(seo_key)
    data = request_url_by_cache(url)
    bs = BeautifulSoup(data, "lxml")
    contents = [(x.attrs['class'][0], x.attrs['onclick']) for x in bs.select('#podcast > ul.showLinks > li > a')]
    links = []
    for cls, content in contents:
        m = regexp.search(content)
        if not m: continue
        link = m.group(1)
        links.append((cls, link))
    return url, links


def load_feeds(feed_file, skip):
    feeds = []
    with open(feed_file) as fh:
        for idx, x in enumerate(fh):
            if idx < skip: continue
            js = json.loads(x)
            feeds.append(js)
    return feeds


def download(feed_file, skip):
    feeds = load_feeds(feed_file, skip)
    for idx, feed in enumerate(feeds):
        title = feed['title']
        pid = feed['pid']
        links = search_stitcher(title)
        print(idx, pid, title, links)


def export(feed_file, social_file, skip):
    feeds = load_feeds(feed_file, skip)
    docs = []
    for idx, feed in enumerate(feeds[:2500]):
        title = feed['title']
        pid = feed['pid']
        res = search_stitcher(title)
        doc = {
            'pid': pid,
            'title': title,
        }
        if res:
            url, links = res
            doc['stitcher_url'] = url
            fields = defaultdict(list)
            for type, url in links:
                fields[type].append(url)
            for k, v in fields.items():
                doc[k] = ' '.join(v)

        print('#{} make doc = {}'.format(idx, doc))
        docs.append(doc)
    df = pandas.DataFrame.from_records(docs)
    fields = ['pid', 'title', 'stitcher_url', 'twitter', 'facebook', 'web', 'donate']
    df.to_csv(social_file, header=True, index=False, columns=fields)


def test():
    links = search_stitcher('ted talks')
    print(links)
    links = search_stitcher('joe rogan')
    print(links)
    links = search_stitcher('99% Invisible')
    print(links)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--export', action='store_true')
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--feed-file', action='store')
    parser.add_argument('--social-file', action='store')
    parser.add_argument('--skip', action='store', type=int)
    args = parser.parse_args()
    feed_file = args.feed_file
    social_file = args.social_file
    skip = args.skip

    if args.test:
        test()
    elif args.download:
        download(feed_file, skip)
    elif args.export:
        export(feed_file, social_file, skip)


if __name__ == '__main__':
    main()
