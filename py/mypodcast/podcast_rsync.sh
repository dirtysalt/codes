#!/usr/bin/env bash
# Copyright (C) dirlt

rsync -avrz rss hbproxy:~/www/
rsync -avrz image hbproxy:~/www/
rsync -avrzL mp3 hbproxy:~/www/
