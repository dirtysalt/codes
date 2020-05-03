#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import argparse
import pickle

import jinja2
import pafy


class Channel:
    def __init__(self, id):
        self.id = id
        self.playlists = []

    def fill(self, resp):
        self.title = resp.title
        self.desc = resp.description

    def add_playlist(self, p):
        self.playlists.append(p)


class Playlist:
    def __init__(self):
        self.videos = []

    def fill(self, resp):
        self.id = resp.plid
        self.author = resp.author
        self.title = resp.title
        self.desc = resp.description
        self.thumbnail = resp.thumbnail

    def add_video(self, v):
        self.videos.append(v)


class Video:
    def __init__(self):
        pass

    def fill(self, resp):
        self.id = resp.videoid
        self.title = resp.title
        self.description = resp.description
        self.duration = resp.duration
        self.watchv_url = resp.watchv_url


def parse_channel(channel_id):
    channel = Channel(channel_id)
    print('get channel {} ...'.format(channel_id))
    resp = pafy.get_channel(channel_id)
    channel.fill(resp)

    print('get playlists ...')
    for x in resp.playlists:
        p = Playlist()
        p.fill(x)
        channel.add_playlist(p)
        print('get videos of playlist {}'.format(p.id))
        for x2 in x:
            v = Video()
            v.fill(x2)
            p.add_video(v)
    print('OK!!!')
    return channel


def save_channel(channel):
    path = 'channel-{}.pkl'.format(channel.id)
    with open(path, 'wb') as fh:
        pickle.dump(channel, fh)


def load_channel(channel_id):
    path = 'channel-{}.pkl'.format(channel_id)
    with open(path, 'rb') as fh:
        channel = pickle.load(fh)
    return channel


ORG_TEMPLATE = """#+title: {{ channel.title }}
https://www.youtube.com/channel/{{ channel.id }}/playlists

{{ channel.description }}

{% for p in channel.playlists %}
** {{ p.title }}
https://www.youtube.com/playlist?list={{ p.id }}

{{ p.description }}

{{ p.thumbnail }}

{% for v in p.videos %}
*** {{ v.title }}

{{ v.watchv_url }}

#+BEGIN_EXPORT HTML
{{ v.description.replace("\n", "</br>") }}</br></br>
#+END_EXPORT

{% endfor %}

{% endfor %}
"""


def export_orgfile(channel):
    path = 'channel-{}.org'.format(channel.id)
    template = jinja2.Template(ORG_TEMPLATE)
    output = template.render(channel=channel)
    with open(path, 'w') as fh:
        fh.write(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump-channel", action='store_true')
    parser.add_argument('--export-orgfile', action='store_true')
    parser.add_argument('--channel-id', action='store')
    args = parser.parse_args()

    if args.dump_channel:
        channel = parse_channel(args.channel_id)
        save_channel(channel)
    if args.export_orgfile:
        channel = load_channel(args.channel_id)
        export_orgfile(channel)


if __name__ == '__main__':
    main()
