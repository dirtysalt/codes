#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import hashlib

import pymongo
import requests
from bs4 import BeautifulSoup


def get_sha1_key(s):
    return hashlib.sha1(s.encode('utf8')).hexdigest()


cache_client = pymongo.MongoClient()
cache_db = cache_client['test']
cache_table = cache_db['cache_table']
force_fetch = False


def request_with_cache(url):
    cache_id = get_sha1_key(url)
    r = cache_table.find_one({'_id': cache_id})
    if r and not force_fetch: return r['data']
    r = requests.get(url)
    if r.status_code != 200:
        return None
    content = r.content
    cache_table.update_one({'_id': cache_id}, {'$set': {'data': content}}, upsert=True)
    return content


def norm_url(url):
    if not url.startswith('http'):
        url = 'https://aws.amazon.com' + url
    q = url.find('?')
    if q != -1:
        url = url[:q]
    return url


def bad_url(url):
    for k in ('marketplace', 'cn/mp/', 'gettting-started'):
        if url.find(k) != -1:
            return True
    return False


def crawl_portal():
    portal_url = 'https://aws.amazon.com/cn/products/'
    bs = make_bs(request_with_cache(portal_url))
    xs = bs.select('#aws-nav-flyout-2-products')[0].select('.aws-link > a')
    products = [(x.text, x.attrs['data-flyout']) for x in xs]
    res = []
    for product_name, product_id in products:
        x = bs.select('#' + product_id)[0]
        services = []
        xs = x.select('h6 > a')
        product_url = norm_url(xs[0].attrs['href']) if xs else ''
        if product_url == portal_url:
            product_url = ''
        if bad_url(product_url):
            continue
        xs = x.select('.aws-link > a')
        for x in xs:
            service_url = norm_url(x.attrs['href'])
            service_name = x.contents[0]
            if bad_url(service_url):
                continue
            services.append({'name': service_name, 'url': service_url})
        if not services:
            continue
        doc = {'name': product_name, 'url': product_url, 'services': services}
        res.append(doc)
    return res


def make_bs(content):
    return BeautifulSoup(content, 'lxml')


def get_text(bs):
    head = bs.head
    xs = [x.attrs.get('content') for x in head.select('meta') if x.attrs.get('name') == 'description']
    description = xs[0] if xs else ''
    description = description.strip()
    text = [description]
    text.extend([x for x in [x.text.strip() for x in bs.findAll('p')] if x])
    return text


N = 200


def crawl_products(products):
    for prod in products[:N]:
        for srv in prod['services']:
            bs = make_bs(request_with_cache(srv['url']))
            text = get_text(bs)
            srv['text'] = text
            # print('====={}====='.format(srv['name']))
            # print(srv['url'])
            # print(text)


products = crawl_portal()
# pprint.pprint(products)
crawl_products(products)

with open('aws-products.org', 'w') as fh:
    fh.write('#+title: AWS Products\n')
    for p in products[:N]:
        if p['url']:
            fh.write('* [[{}][{}]]\n'.format(p['url'], p['name']))
        else:
            fh.write('* {}\n'.format(p['name']))
        for srv in p['services']:
            fh.write('** [[{}][{}]]\n'.format(srv['url'], srv['name']))
            text = srv['text']
            tmp = ""
            for x in text:
                if len(x) >= 50:
                    tmp += '{}\n\n'.format(x)
            if tmp:
                fh.write('#+BEGIN_QUOTE\n{}#+END_QUOTE\n\n'.format(tmp))
