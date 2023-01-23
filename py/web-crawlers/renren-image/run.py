#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import gevent
import gevent.monkey
gevent.monkey.patch_all()
print('gevent.monkey patched')

from gevent.pool import Pool as ThreadPool

import re
import os
import json
import string
import pymongo

import requests
from bs4 import BeautifulSoup
import hashlib

STATION_ID = 600261907

mongo_client = pymongo.MongoClient()
mongo_db = mongo_client.rr_image
cache_table = mongo_db['cache_%d' % STATION_ID]

CACHE_DIR = 'cache-%d/' % (STATION_ID)
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

OUTPUT_DIR = 'output-%d/' % (STATION_ID)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_url(url, ss = None):
    if not ss:
        ss = requests.session()
    key = hashlib.md5(url).hexdigest()
    r = cache_table.find_one({'_id': key})
    if r: return r['data']
    print('get url %s' % url)
    r = ss.get(url)
    data = r.content
    cache_table.insert({'_id': key, 'data': data})
    return data

def get_album_urls():
    cache = CACHE_DIR + 'album.urls.txt'
    if not os.path.exists(cache):
        ss = requests.session()
        urls = []
        init_url = 'http://page.renren.com/%d/album' % STATION_ID

        def f(url, init = False):
            data = get_url(url, ss)
            bs = BeautifulSoup(data)
            xs = bs.select('#tabBody > div > div > div > table > tbody > tr > td > div > a')
            for x in xs:
                path = x.attrs['href']
                urls.append('http://page.renren.com' + path)
            if init:
                xs = bs.select('#tabBody > div > div > div > ol > li > a')
                last_page = int(xs[-1].attrs['href'].split('=')[-1])
                return last_page

        last_page = f(init_url, True)
        for x in range(1, last_page + 1):
            url = init_url + '?curpage=%d' % x
            f(url)

        with open(cache, 'w') as fh:
            fh.writelines([x + '\n' for x in urls])
        return urls

    with open(cache) as fh:
        return [x.strip() for x in fh]

def get_image_urls(album_url):
    album_id = album_url.split('/')[-1]
    cache = CACHE_DIR + 'album.urls.%s.txt' % album_id
    if os.path.exists(cache):
        with open(cache) as fh:
            return [x.strip() for x in fh]

    curpage = 0
    ss = requests.session()
    images = []
    while True:
        url = album_url + '?curpage=%d' % curpage
        data = get_url(url, ss)
        bs = BeautifulSoup(data)
        xs = bs.select('#single-column > table > tbody > tr > td > a')
        for x in xs:
            images.append('http://page.renren.com' + x.attrs['href'])
        # 最后一页
        xs = bs.select('#content > div.pager-top > ol > li > a')
        if not xs or 'class' not in xs[-1].attrs:
            break
        curpage += 1

    with open(cache, 'w') as fh:
        fh.writelines([x + '\n' for x in images])
    return images

DOWNLOAD_URL_RE = re.compile(r'"large":"([^"]+)"')

def download_images(image_urls):
    def f(url):
        ss = requests.session()
        data = get_url(url, ss)
        m = re.search(DOWNLOAD_URL_RE, data)
        if not m: return
        data_url = m.groups()[0].replace('\\', '')

        file_name = url.split('/')[-1]
        file_path = os.path.join(OUTPUT_DIR, file_name + '.jpg')
        if os.path.exists(file_path):
            # print('cached...')
            return
        r = ss.get(data_url)
        print('download image %s' % data_url)
        with open(file_path, 'wb') as fh:
            fh.write(r.content)

    tp = ThreadPool(4)
    for url in image_urls:
        tp.spawn(f, url)
    tp.join()

if __name__ == '__main__':
    album_urls = get_album_urls()
    image_urls = []
    for album_url in album_urls:
        image_urls.extend(get_image_urls(album_url))
    download_images(image_urls)
