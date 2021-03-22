#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import http.cookiejar
import requests
from bs4 import BeautifulSoup
import pickle
import jinja2
import traceback

import os
if not os.path.exists('cache_dir'):
    os.makedirs('cache_dir')

def get_article_links():
    data = open('wenzhang_full.html').read()
    bs = BeautifulSoup(data)
    links = [x.attrs['href'] for x in bs.select('._photoLink')]
    links = [x for x in links if x.startswith('http://wenzhang.baidu.com') or \
                   x.startswith('https://wenzhang.baidu.com')]
    return links

def link_to_cache_key(link):
    return link[-27:-11]

def cache_file_path(key):
    return 'cache_dir/' + key

def download_article(ss, link):
    cache_key = link_to_cache_key(link)
    cache_file = cache_file_path(cache_key)
    if os.path.exists(cache_file):
        return

    r = ss.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    r2 = ss.get(soup.body.iframe["src"])
    with open(cache_file, 'w') as fh:
        fh.write(r2.content)
    return

def do_donwload(links):
    ss = requests.session()
    cj = http.cookiejar.LWPCookieJar()
    cj.load('cookies.txt', ignore_discard = True, ignore_expires = True)
    ss.cookies = cj

    for link in links:
        print('downloading %s' % link)
        download_article(ss, link)

def generate_single_html(links):
    template = jinja2.Template("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>

<body>
<h1>TOC</h1>
<div>
<ul>
{% for (idx, title, _) in items %}
<li><a href="#{{ idx }}">{{ title }}</a></li>
{% endfor %}
</ul>
</div>
<hr/>

{% for (idx, title, content) in items %}
<div>
<a name="{{ idx }}"><h2>{{ title }}</h2></a>
{{ content }}
</div>
<hr/>
{% endfor %}
""")
    items = []
    idx = 0
    for link in links:
        cache_key = link_to_cache_key(link)
        cache_file = cache_file_path(cache_key)
        bs = BeautifulSoup(open(cache_file).read())
        try:
            date = bs.select('.time-cang')[0].text
            title = bs.select('.pcs-article-title_ptkaiapt4bxy_baiduscarticle')[0].text
            content = bs.select('.pcs-article-content_ptkaiapt4bxy_baiduscarticle')[0]
            items.append((idx, '%s - %s' % (title, date), content))
            idx += 1
        except:
            traceback.print_exc()
            print "problematic link = %s. try to remove '%s' and run it again." % (link, cache_file)
            return

    output = template.render(items = items)
    with open('output.html', 'w') as fh:
        fh.write(output.encode('utf-8'))

def main():
    links = get_article_links()
    do_donwload(links)
    generate_single_html(links)

if __name__ == '__main__':
    main()
