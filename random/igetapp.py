#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import glob
import hashlib
import io
import jinja2
import json
import os
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

style_string = """
<style type="text/css">html {
    font-family: Georgia, "Microsoft Yahei", "WenQuanYi Micro Hei";
}

/* pre { */
/*     background-color: #eee; */
/*     box-shadow: 5px 5px 5px #888; */
/*     border: none; */
/*     padding: 5pt; */
/*     margin-bottom: 14pt; */
/*     color: black; */
/*     padding: 12pt; */
/*     font-family: Consolas; */
/*     font-size: 95%; */
/*     overflow: auto; */
/* } */

.title  { /* text-align: center; */
          margin-bottom: 1em; }
.subtitle { /* text-align: center; */
            font-size: medium;
            font-weight: bold;
            margin-top:0; }
.todo   { font-family: monospace; color: red; }
.done   { font-family: monospace; color: green; }
.priority { font-family: monospace; color: orange; }
.tag    { background-color: #eee; font-family: monospace;
          padding: 2px; font-size: 80%; font-weight: normal; }
.timestamp { color: #bebebe; }
.timestamp-kwd { color: #5f9ea0; }
.org-right  { margin-left: auto; margin-right: 0px;  text-align: right; }
.org-left   { margin-left: 0px;  margin-right: auto; text-align: left; }
.org-center { margin-left: auto; margin-right: auto; text-align: center; }
.org-ul { padding-left: 10px; }
.org-ol { padding-left: 20px; }
ul { padding-left: 10px; }
ol { padding-left: 20px; }

.underline { text-decoration: underline; }
#postamble p, #preamble p { font-size: 90%; margin: .2em; }
p.verse { margin-left: 3%; }
pre {
    border: 1px solid #ccc;
    box-shadow: 3px 3px 3px #eee;
    padding: 8pt;
    font-family: monospace;
    overflow: auto;
    margin: 1.2em;
}
pre.src {
    position: relative;
    overflow: visible;
    padding-top: 1.2em;
}
pre.src:before {
    display: none;
    position: absolute;
    background-color: white;
    top: -10px;
    right: 10px;
    padding: 3px;
    border: 1px solid black;
}
pre.src:hover:before { display: inline;}
pre.src-sh:before    { content: 'sh'; }
pre.src-bash:before  { content: 'sh'; }
pre.src-emacs-lisp:before { content: 'Emacs Lisp'; }
pre.src-R:before     { content: 'R'; }
pre.src-perl:before  { content: 'Perl'; }
pre.src-java:before  { content: 'Java'; }
pre.src-sql:before   { content: 'SQL'; }

table { border-collapse:collapse; }
caption.t-above { caption-side: top; }
caption.t-bottom { caption-side: bottom; }
td, th { vertical-align:top;  }
th.org-right  { text-align: center;  }
th.org-left   { text-align: center;   }
th.org-center { text-align: center; }
td.org-right  { text-align: right;  }
td.org-left   { text-align: left;   }
td.org-center { text-align: center; }
dt { font-weight: bold; }
.footpara { display: inline; }
.footdef  { margin-bottom: 1em; }
.figure { padding: 1em; }
.figure p { /* text-align: center; */ }
.inlinetask {
    padding: 10px;
    border: 2px solid gray;
    margin: 10px;
    background: #ffffcc;
}
#org-div-home-and-up
{ text-align: right; font-size: 70%; white-space: nowrap; }
textarea { overflow-x: auto; }
.linenr { font-size: smaller }
.code-highlighted { background-color: #ffff00; }
.org-info-js_info-navigation { border-style: none; }
#org-info-js_console-label
{ font-size: 10px; font-weight: bold; white-space: nowrap; }
.org-info-js_search-highlight
{ background-color: #ffff00; color: #000000; font-weight: bold; }

/* http://www.yinwang.org/main.css */

body {
    /* font-family:"lucida grande", "lucida sans unicode", lucida, helvetica, "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif; */
    font-size: 18px;
    margin: 5% 5% 5% 5%;
    padding: 2% 5% 5% 5%;
    width: 80%;
    line-height: 150%;
    border: 1px solid LightGrey;
}

H1 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
}

H2 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-bottom: 60px;
    margin-bottom: 40px;
    padding: 5px;
    border-bottom: 2px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


H3 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-top: 40px;
    margin-bottom: 30px;
    border-bottom: 1px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


H4 {
    /* font-family: "Palatino Linotype", "Book Antiqua", Palatino, Helvetica, STKaiti, SimSun, serif; */
    margin-top: 40px;
    margin-bottom: 30px;
    border-bottom: 1px LightGrey solid;
    width: 98%;
    line-height: 150%;
    color: #666666;
}


li {
    margin-left: 10px;
}


blockquote {
    border-left: 4px lightgrey solid;
    padding-left: 5px;
    margin-left: 20px;
}


pre {
    font-family: Inconsolata, Consolas, "DEJA VU SANS MONO", "DROID SANS MONO", Proggy, monospace;
    font-size: 75%;
    border: solid 1px lightgrey;
    background-color: Ivory;
    padding: 5px;
    line-height: 130%;
    margin-left: 10px;
    width: 95%;
}


code {
    font-family: Inconsolata, Consolas, "DEJA VU SANS MONO", "DROID SANS MONO", Proggy, monospace;
    font-size: 90%;
}


a {
    text-decoration: none;
    # cursor: crosshair;
    border-bottom: 1px dashed Red;
    padding: 1px;
    # color: black;
}


a:hover {
	background-color: LightGrey;
}


img {
    box-shadow: 0 0 10px #555;
    border-radius: 6px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 10px;
    margin-bottom: 10px;
    -webkit-box-shadow: 0 0 10px #555;
    width: 100%;
    max-width: 600px;
}

img.displayed {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

#table-of-contents {
    border-bottom: 2px LightGrey solid;
}</style>
"""


def get_sha1_key(s):
    return hashlib.sha1(s.encode('utf8')).hexdigest()


def parse_response(resp):
    path = resp
    data = open(resp).read()
    resp = json.loads(data)
    # create_time = resp['data']['article']['CreateTime']
    create_time = resp['data']['article']['PublishTime']
    d = resp['data']['content']
    js = json.loads(d)
    title = js['title']
    content = js['content']
    fh = io.StringIO()
    for c in content:
        ct = c['type']
        if ct == 'title':
            fh.write('<h2>{}</h2>'.format(c['value']))
        elif ct == 'text':
            fh.write(c['value'])
        elif ct == 'image':
            url = c['src']
            key = get_sha1_key(url)
            path = 'images/{}.jpg'.format(key)
            if not os.path.exists(path):
                print('downloading url = {}'.format(url))
                r = requests.get(url, verify = False)
                with open(path, 'wb') as img:
                    img.write(r.content)
            # fh.write('<img src="{}"/>'.format(url))
            fh.write('<img src="{}"/>'.format(path))
        elif ct in ('comment',):
            fh.write('<blockquote><p>{}</p></blockquote>'.format('</br>'.join(c['value'])))
        elif ct in ('split', 'center'):
            fh.write('<hr/>')
        elif ct in( 'tip' ,'center', 'quotedNew'):
            fh.write(c['value'])
        elif ct in ('elite',):
            fh.write('<p>{}</p>'.format(c['value'].replace('\n', '</br>')))
        elif ct in ('quotedOnlyBlack', 'quotedOnlyGray'):
            fh.write('<blockquote><p>{}</p></blockquote>'.format(c['value'].replace('\n', '</br>')))
        elif ct in ('audio', 'quoted'):
            pass
        else:
            print(c)
            pass
        fh.write('\n')
    return create_time, title, fh.getvalue()


sp_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ single_page_title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="dirtysalt" />
{{ style_string }}
</head>

<body>
<div id="content">
<h1 class="title">{{ single_page_title }}</h1>
<div id="table-of-contents">
<h2>Table of Contents</h2>
<ul>
{% for x in items %}
<li><a href="#anchor{{ x.idx }}">{{ x.title }}</a></li>
{% endfor %}
</ul>
</div>

{% for x in items %}
<div class="outline-2">
<h2 id="anchor{{ x.idx }}">{{ x.title }}<a href="#table-of-contents">#</a></h2>
<div class="outline-text-2">
{{ x.html }}
</div>
</div>
{% endfor %}

</div>
</body>
</html>
"""

index_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ index_page_title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="dirtysalt" />
{{ style_string }}
</head>

<body>
<div id="content">
<h1 class="title">{{ index_page_title }}</h1>
<p><a href="sp.html">Single Page Document</a></p>
<ul>
{% for x in items %}
<li><a href="{{ x.href }}">{{ x.title }}</a></li>
{% endfor %}
</ul>
</div>
</body>
</html>
"""

page_string = """
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<meta  http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta  name="viewport" content="width=device-width, initial-scale=1" />
<title>{{ title }}</title>
<meta  name="generator" content="Org-mode" />
<meta  name="author" content="dirtysalt" />
{{ style_string }}
</head>

<body>

<div class="outline-2">
<h2>{{ title }}</h2>
<div class="outline-text-2">
{{ html }}
</div>
</div>

</body>
</html>
"""

download_audio_script_string = """#!/bin/bash
mkdir -p audio/
{% for (idx,x) in items %}
wget --continue "{{ x.url }}" -O "audio/{{ "%03d"|format(idx) }}-{{ x.title }}.mp3"
{% endfor %}
"""


def make_download_audio_script():
    if not os.path.exists('info/'):
        return

    fs = glob.glob('info/*') + glob.glob('info/article/*')
    items = []
    for f in fs:
        js = json.load(open(f))
        if 'audio' in js['c']['article_info']:
            create_time = js['c']['article_info']['create_time']
            url = js['c']['article_info']['audio']['mp3_play_url']
            title = js['c']['article_info']['audio']['title']
            items.append({'title': title, 'url': url, 'create_time': create_time})
    items.sort(key = lambda x: x['create_time'])
    template = jinja2.Template(download_audio_script_string)
    output = template.render(items=list(enumerate(items)))
    with open('download_audio.sh', 'w') as fh:
        fh.write(output)


def main():
    fs = glob.glob('resp/get*')
    items = []
    dup = set()
    os.makedirs('html', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    template = jinja2.Template(page_string)
    for resp in fs:
        create_time,title, html = parse_response(resp)
        if title in dup: continue
        dup.add(title)
        path = "html/{}.html".format(title)
        with open(path, 'w') as fh:
            output = template.render(style_string=style_string,
                                     title=title,
                                     html=html)
            output = output.replace('images/', '../images/')
            fh.write(output)
        items.append((title, html, path, create_time))
    items.sort(key=lambda x: x[-1])

    items = [{'title': x[0], 'html': x[1], 'idx': idx, 'href': x[2]} for (idx, x) in enumerate(items)]

    template = jinja2.Template(sp_string)
    with open('sp.html', 'w') as fh:
        output = template.render(items=items, style_string=style_string,
                                 single_page_title="Single Page Document")
        fh.write(output)

    template = jinja2.Template(index_string)
    with open('index.html', 'w') as fh:
        output = template.render(items=items, style_string=style_string,
                                 index_page_title="Index Page Document")
        fh.write(output)

    make_download_audio_script()


if __name__ == '__main__':
    main()
