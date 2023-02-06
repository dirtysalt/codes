#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import email
import email.utils
import glob
import hashlib
import os
import sys
import time
import uuid
from datetime import datetime, timedelta
from urllib.parse import quote
from jinja2 import Template
import subprocess
import json

# ============================================================

def get_audio_duration(f):
    input_filename = "input.mp4"
    out = subprocess.check_output(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", f])
    ffprobe_data = json.loads(out)
    duration_seconds = float(ffprobe_data["format"]["duration"])
    print("[get_audio_duration] f = %s, duration = %.2f" % (f, duration_seconds))
    return duration_seconds


def audio_duration_in_text(v):
    return '%02d:%02d:%02d' % (v / 3600, (v % 3600) / 60, v % 60)


def get_file_size(f):
    return os.path.getsize(f)


def to_rfc822_datetime(nowdt):
    nowtuple = nowdt.timetuple()
    nowtimestamp = time.mktime(nowtuple)
    return email.utils.formatdate(nowtimestamp)


def get_sha1_key(s):
    return hashlib.sha1(s).hexdigest()


def gen_uuid(s):
    x = uuid.uuid3(uuid.NAMESPACE_DNS, s)
    return str(x)

# ============================================================


RSS_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:atom="http://www.w3.org/2005/Atom"
     version="2.0">
    <channel>
        <atom:link href="http://{{ domain }}/rss/{{ name }}.xml" type="application/rss+xml" rel="self"/>
        <copyright>{{ author }}</copyright>
        <link>{{ link }} </link>
        <language>{{ language or "zh-cn"}}</language>

        <title>{{ title }}</title>
        <description>{{ description }}</description>
        <pubDate>{{ releaseDate }}</pubDate>

        <itunes:summary>{{ summary }}</itunes:summary>
        <itunes:subtitle>{{ subtitle }}</itunes:subtitle>
        <itunes:author>{{ author }}</itunes:author>
        <itunes:image href="{{ image_url }}"/>
        <itunes:owner>
            <itunes:name>{{ author }}</itunes:name>
            <itunes:email>{{ email }}</itunes:email>
        </itunes:owner>
        <itunes:keywords>{{ keywords }}</itunes:keywords>
        <itunes:category text="Education"/>
        <itunes:explicit>no</itunes:explicit>

        {% for t in tracks %}
        <item>
            <title>{{ t.title }}</title>
            <description>{{ t.description }}</description>
            <itunes:summary>{{ t.summary }}</itunes:summary>
            <itunes:image href="{{ t.image_url }}"/>
            <!-- <itunes:order>{{ t.itunes_order }}</itunes:order> -->
            <enclosure url="{{ t.audio_url }}" type="audio/mp3" length="{{ t.audio_size or 0}}"/>
            <itunes:duration>{{ t.audio_duration_text or 0 }}</itunes:duration>
            <guid isPermaLink="false">{{ t.guid }}</guid>
            <pubDate>{{ t.releaseDate }}</pubDate>
            <itunes:explicit>no</itunes:explicit>
        </item>
        {% endfor %}
    </channel>
</rss>
"""

rss_template = Template(RSS_TEMPLATE)


def run(ctx):
    mp3_dir = ctx['mp3_dir']

    myfiles = []
    for ext in ('mp3', 'm4a', 'mp4'):
        myfiles += glob.glob(os.path.join(mp3_dir, ctx['name'], '*.' + ext))

    # sort by filename
    myfiles.sort()

    now = datetime.now()
    ctx['tracks'] = []
    ctx['description'] = '<br/>\n'.join(['{}. {}'.format(x[0] + 1, os.path.basename(x[1])) for x in enumerate(myfiles)])
    ctx['releaseDate'] = to_rfc822_datetime(now)
    ctx['image_url'] = 'http://{}/image/{}.jpg'.format(ctx['domain'], ctx['name'])

    tracks = ctx['tracks']
    for order, name in enumerate(myfiles):
        base_name = os.path.basename(name)
        t = {
            'title': base_name,
            'audio_url': 'http://{}/'.format(ctx['domain']) + quote('mp3/{}/{}'.format(ctx['name'], base_name)),
            'audio_size': get_file_size(name),
            'audio_duration_text': audio_duration_in_text(get_audio_duration(name)),
            'guid': gen_uuid(name),
            'releaseDate': to_rfc822_datetime(now - timedelta(hours=order)),
            'itunes_order': order + 1,
            'image_url': ctx['image_url']
        }
        tracks.append(t)

    rss = rss_template.render(**ctx)

    if tracks:
        with open(os.path.join(ctx['rss_dir'], '%s.xml' % ctx['name']), 'w') as fh:
            fh.write(rss)
        print('rss url = http://{}/rss/{}.xml'.format(ctx['domain'], ctx['name']))
    else:
        print("No available episode for '%s'" % (ctx['name']))


# ============================================================
"""
# Example configuration.
sites = {
    'TestFeed': {
        'title': '这是测试站点',
    },
}

glob = {
  'author': 'dirtysalt',
  'email': 'dirtysalt1987@gmail.com',
  'domain': 'dirtysalt.github.io',
  'mp3_dir': 'mp3',
  'rss_dir': 'rss'
}
"""


def main():
    import config
    sites = config.sites
    glob = config.glob
    reqs = sites.keys() if len(sys.argv) == 1 else sys.argv[1:]

    for site in reqs:
        if site not in sites: continue
        print('Generating RSS XML for {}'.format(site))
        ctx = glob.copy()
        ctx.update(sites[site])
        # use site id as name
        ctx['name'] = site
        run(ctx)

if __name__ == '__main__':
    main()
