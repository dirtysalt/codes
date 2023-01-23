#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import argparse
from gevent import monkey
from queue import Queue

monkey.patch_all()

from gevent.pool import Pool

import hashlib
import os

import requests
from bs4 import BeautifulSoup

CACHE_DIR = './cache/'
MARKDOWN_DIR = './md/'


def ensure_dir_existed(path):
    if not os.path.exists(path):
        os.makedirs(path)


ensure_dir_existed(CACHE_DIR)
ensure_dir_existed(MARKDOWN_DIR)


def get_md5_key(s):
    return hashlib.md5(s.encode('utf8')).hexdigest()


def generate_dates(f, t):
    dates = []
    for y in range(f, t + 1):
        for m in range(12):
            dates.append((y, m + 1))

    return reversed(dates)


def parse_permlinks(y, m):
    name = 'permlinks_{}_{:02d}.txt'.format(y, m)
    path = CACHE_DIR + name
    if os.path.exists(path):
        print('permlinks cached: {}'.format(name))
        with open(path) as fh:
            links = [x.strip() for x in fh]

    else:
        url = 'https://blog.codingnow.com/{}/{:02d}/'.format(y, m)
        print('parse permlinks: {}'.format(url))
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        xs = bs.select('.permalink')
        links = [x.attrs['href'] for x in xs]
        with open(path, 'w') as fh:
            fh.writelines([x + '\n' for x in links])

    return links

def download_link(url):
    print('download url: {}'.format(url))
    key = get_md5_key(url)
    path = CACHE_DIR + key
    if os.path.exists(path):
        print('url cached: {}'.format(url))
        with open(path, 'rb') as fh:
            data = fh.read()
    else:
        r = requests.get(url)
        with open(path, 'wb') as fh:
            fh.write(r.content)
            data = r.content

    bs = BeautifulSoup(data, "lxml")
    title = bs.select('.entry-header')[0].text
    body = bs.select('.entry-body')
    more = bs.select('.entry-more')
    content = ''

    def flt(z):
        return True

    def fmt(z):
        if hasattr(z, 'name'):
            if z.name in ('pre', 'mtc:block'):
                return "```\n" + z.text + "```\n"
            elif z.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                return ('#' * (int(z.name[1:]) + 1)) + ' ' + z.text + '\n'
        content = str(z)
        replaces = (
            ('"*"', '"\*"'),
            ('"**"', '"\*\*"'),
            ('*)', '\*)'),
            (' * ',' \* ')
        )
        for f, t in replaces:
            content = content.replace(f, t)
        return content

    for x in body + more:
        content += '\n'.join(fmt(z) for z in x.children if flt(z))

    return title, content

toc = []


def write_markdown(title, content, year, month, idx, url):
    name = '{}-{:02d}-{:03d}.md'.format(year, month, idx)
    toc.append((name, year, month, title, url))
    print('write markdown: {}'.format(name))
    path = MARKDOWN_DIR + name
    content = f"# {title}-{name}\n\n{content}\n\n"
    with open(path, 'w') as fh:
        fh.write(content)


def handle_event(queue: Queue):
    item = queue.get()
    print(item)
    if item[0] == 'permlinks':
        y, m = item[1:]
        permlinks = parse_permlinks(y, m)
        for idx, link in enumerate(permlinks):
            event = ['download', idx, link, y, m]
            print(event)
            queue.put(event)

    elif item[0] == 'download':
        idx, link, y, m = item[1:]
        title, content = download_link(link)
        write_markdown(title, content, y, m, idx, link)

    else:
        raise RuntimeError(item)
    queue.task_done()


def handle_event_loop(queue: Queue):
    while not queue.empty():
        handle_event(queue)


# def main():
#     for y, m in generate_dates():
#         permlinks = parse_permlinks(y, m)
#         for idx, link in enumerate(permlinks):
#             title, content = download_link(link)
#             write_markdown(title, content, y, m, idx)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fm', action='store', default=2005, type=int)
    parser.add_argument('--to', action='store', default=2019, type=int)
    args = parser.parse_args()

    queue = Queue()
    pool = Pool(32)
    for i in range(32):
        pool.spawn(handle_event_loop, queue)

    for y, m in generate_dates(args.fm, args.to):
        queue.put(['permlinks', y, m])

    queue.join()

    toc.sort(key = lambda x: x[0], reverse = True)
    path = 'index.md'
    last_year = None
    with open(path, 'w') as fh:
        fh.write('# 文章目录\n')
        for (name, y, m, title, url) in toc:
            if y != last_year:
                fh.write('\n## {}\n'.format(y))
                last_year = y

            fh.write("- [{}]({})\n".format(title, url))


if __name__ == '__main__':
    main()

# print(parse_permlinks(2009, 11))
# print(download_link('https://blog.codingnow.com/2009/03/oaaoeueoeaeeaaeace.html'))
