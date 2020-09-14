#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os
import pprint
import random
import sys

import bencode

pp = pprint.PrettyPrinter(indent=2)


def is_video(ext_name):
    return ext_name in ('.wmv', '.avi', '.rmvb', '.rm', '.mkv', '.mp4', '.3gp', '.MOV', '.mkv', '.flv', '.mp4',)


def cleanse(input_file, output_file, prefix, keep_video_name):
    s = open(input_file).read()
    d = bencode.bdecode(s)
    # pp.pprint(d)
    # print('--------------------')
    # pp.pprint(d['info']['files'])

    d['info']['name'] = prefix
    d['info']['name.utf-8'] = prefix
    if 'comment' in d:
        del d['comment']
    if 'comment.utf-8' in d:
        del d['comment.utf-8']
    nfiles = []
    idx = 0
    if 'files' in d['info']:
        for f in d['info']['files']:
            vd = False
            if 'path' in f:
                name = f['path'][-1]
                (_, ext) = os.path.splitext(name)
                if is_video(ext):
                    if not keep_video_name:
                        name = '%s-%d%s' % (prefix, idx, ext)
                    idx += 1
                    path = [name]
                    f['path'] = path
                    f['path.utf-8'] = path
                    nfiles.append(f)
                    vd = True
            if not vd:
                f['path'] = ['null']
                f['path.utf-8'] = ['null']
                nfiles.append(f)
        d['info']['files'] = nfiles
    else:
        d['info']['name'] += '.rmvb'
        d['info']['name.utf-8'] += '.rmvb'
    # print('--------------------')
    # pp.pprint(d['info']['files'])
    s = bencode.bencode(d)
    open(output_file, 'w').write(s)


if __name__ == '__main__':
    argc = 1
    prefix = 'AV-%03d' % (random.randint(0, 1000))
    keep_video_name = False
    while argc < len(sys.argv):
        argv = sys.argv[argc]
        if argv == '-i':
            input_file = sys.argv[argc + 1]
            argc += 1
        elif argv == '-o':
            prefix = sys.argv[argc + 1]
            argc += 1
        elif argv == '-k':
            keep_video_name = True
        else:
            print('torrent cleanser')
            print('usage: %s -i <input-file> -o <output-file> [-k]' % (sys.argv[0]))
            exit(-1)
        argc += 1
    (path, _) = os.path.split(input_file)
    outfname = os.path.join(path, '%s.torrent' % (prefix))
    cleanse(input_file, outfname, prefix, keep_video_name)
