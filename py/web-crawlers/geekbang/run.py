#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import json
import os
import time

import config
import const as C
import jinja2
import requests

true = True
false = False
null = None

projects = {
    'mysql': 139,
    'aitech': 43,
    'recsys': 74,
    'arch': 166,
    'coolshell': 48,
    'techbiz': 42,
}


def ensure_dir_existed(path):
    if not os.path.exists(path):
        os.makedirs(path)


def make_session():
    session = requests.Session()
    session.headers = {
        'Origin': 'https://time.geekbang.org',
        'Cookie': config.COOKIE,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    return session


def get_post_url(post_id):
    url = 'https://time.geekbang.org/column/article/{}'.format(post_id)
    return url


ss = make_session()


def _get_articles(cid):
    url = 'https://time.geekbang.org/serv/v1/column/articles'
    data = {"cid": cid, "size": 100, "prev": 0, "order": "earliest", "sample": false}
    print(url, data)
    r = ss.post(url, json=data)
    if r.status_code != 200:
        print(r.json())
        raise RuntimeError()
    docs = r.json()['data']['list']
    res = [
        dict(post_id=d['id'], title=d['article_title'])
        for d in docs
    ]
    return res


def get_articles(path, cid):
    ensure_dir_existed(path)
    cache_path = os.path.join(path, 'index.json')
    if not os.path.exists(cache_path):
        res = _get_articles(cid)
        with open(cache_path, 'w') as fh:
            json.dump(res, fh)
    else:
        with open(cache_path, 'r') as fh:
            res = json.load(fh)
    return res


def _get_article(post_id):
    url = 'https://time.geekbang.org/serv/v1/article'
    data = {"id": post_id, "include_neighbors": true, "is_freelyread": true}
    print(url, data)
    r = ss.post(url, json=data, headers={'Referer': get_post_url(post_id)})
    if r.status_code != 200:
        print(r.content)
        raise RuntimeError()
    data = r.json()['data']
    return data


def get_article(path, post_id):
    print('get post {}'.format(post_id))
    ensure_dir_existed(path)
    cache_path = os.path.join(path, '{}.json'.format(post_id))
    if not os.path.exists(cache_path):
        res = _get_article(post_id)
        time.sleep(2)
        with open(cache_path, 'w') as fh:
            json.dump(res, fh)
    else:
        with open(cache_path, 'r') as fh:
            res = json.load(fh)
    return res


def run(project):
    cache_path = '{}/cache'.format(project)
    cid = projects[project]
    res = get_articles(cache_path, cid)
    for d in res:
        post_id = d['post_id']
        try:
            get_article(cache_path, post_id)
        except:
            pass

    html_path = '{}/html'.format(project)
    os.makedirs(html_path, exist_ok=True)
    template = jinja2.Template(C.page_string)
    dup = set()
    items = []
    for d in res:
        post_id = d['post_id']
        data = get_article(cache_path, post_id)
        title, html = data['article_title'], data['article_content']
        if title in dup: continue
        dup.add(title)

        path = os.path.join(html_path, '{}.html'.format(post_id))
        with open(path, 'w') as fh:
            output = template.render(style_string=C.style_string,
                                     title=title,
                                     html=html)
            fh.write(output)
        pub_url = get_post_url(post_id)
        items.append((title, html, path, pub_url))

    items = [{'title': x[0], 'html': x[1], 'idx': idx,
              'pub_url': x[3],
              'href': '/'.join(x[2].split('/')[1:])} for (idx, x) in
             enumerate(items)]

    template = jinja2.Template(C.sp_string)
    with open(os.path.join(project, 'sp.html'), 'w') as fh:
        output = template.render(items=items, style_string=C.style_string,
                                 single_page_title="Single Page Document")
        fh.write(output)

    template = jinja2.Template(C.index_string)
    with open(os.path.join(project, 'index.html'), 'w') as fh:
        output = template.render(items=items, style_string=C.style_string,
                                 index_page_title="Index Page Document")
        fh.write(output)

    template = jinja2.Template(C.index_org_string)
    with open(os.path.join(project, 'index2.org'), 'w') as fh:
        output = template.render(items=items, index_page_title=project)
        fh.write(output)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--project')
    args = parser.parse_args()
    project = args.project
    if project is None:
        import sys
        print('{} --project [PROJECT]'.format(sys.argv[0]))
        for p in projects:
            print('\t' + p)
    else:
        run(project)


if __name__ == '__main__':
    main()
