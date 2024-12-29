#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import gevent
import gevent.monkey

gevent.monkey.patch_all()

import os
import sys
import tempfile
import shlex
import subprocess
import mutagen

from PIL import ExifTags, Image

_null_writer = open('/dev/null', 'w')


def run_shell_command(cmd, stdout=None, stderr=None,
                      cwd=None, timeout=None, debug=False):
    args = shlex.split(cmd)
    if stdout is False:
        stdout = _null_writer
    if stderr is False:
        stderr = _null_writer
    p = subprocess.Popen(args, stdout=stdout, stderr=stderr, cwd=cwd)

    ok = False
    with gevent.Timeout(timeout, False):
        p.wait()
        ok = True

    if not ok:
        p.kill()
        return None
    return p


def get_audio_length(f):
    x = mutagen.mp3.MP3(f)
    return x.info.length


def concate_images(inputs, row, col, height, width, output):
    input_string = ' '.join(inputs)
    cmd = 'montage -mode concatenate -resize %dx%d -tile %dx%d %s %s' % (height, width, row, col, input_string, output)
    p = run_shell_command(cmd)
    return p.returncode == 0


FFMPEG_BIN = 'ffmpeg'
GIFSICLE_LOSSY_BIN = './gifsicle-lossy-mac' if sys.platform == 'darwin' else 'gifsicle-lossy-static'


def to_lossy_gif(mp4, gif, ss=0, to=2, fps=4, lossy=30):
    (fid, tmp) = tempfile.mkstemp(suffix='.png')
    os.close(fid)
    filters = "fps=%.2f,scale=flags=lanczos" % fps
    palette = tmp
    input_file = mp4
    output_file = gif
    cmds = [
        FFMPEG_BIN + ' -v warning -i %(input_file)s -vf "%(filters)s,palettegen" ' +
        '-ss %(ss)d -to %(to)d -y -threads 1 %(palette)s',
        FFMPEG_BIN + ' -v warning -i %(input_file)s -i %(palette)s -filter_complex "' +
        '%(filters)s [x]; [x][1:v] paletteuse" -ss %(ss)d -to %(to)d -threads 1 -y %(output_file)s',
        GIFSICLE_LOSSY_BIN + ' -O3 --lossy=%(lossy)d %(output_file)s -o %(output_file)s']
    try:
        for cmd in cmds:
            c = cmd % (locals())
            p = run_shell_command(c, stderr=False, stdout=False, timeout=30)
            if not p or p.returncode != 0:
                raise Exception('shell command failed. cmd = %s' % c)
    finally:
        os.remove(tmp)


def get_video_length(mp4):
    # pylint: disable=E1101
    p = run_shell_command(conf.FFPROBE_BIN + ' -i %s' % mp4, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    if not p or p.returncode != 0:
        return 0
    xs = map(lambda x: x.strip(), p.stderr.readlines())
    xs2 = filter(lambda x: x.startswith('Duration'), xs)
    if not xs2:
        return 0
    ys = xs2[0].split(' ')
    if len(ys) < 2:
        return 0
    y = ys[1]
    if not re.match(r'\d+:\d+:\d+.\d+,', y):
        return 0
    (a, b) = y[:-1].split('.')
    (h, m, s) = a.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(b) * 0.001


# 保持比例进行图片缩放，其中limit是保证h,w最大值
def scale_image(input_path, output_path, limit=640):
    im = Image.open(input_path)

    # rotate if necessary
    if hasattr(im, '_getexif'):  # only present in JPEGs
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        e = im._getexif()
        if e is not None:
            exif = dict(e.items())
            if orientation in exif:
                orientation = exif[orientation]
                if orientation == 3:
                    im = im.transpose(Image.ROTATE_180)
                elif orientation == 6:
                    im = im.transpose(Image.ROTATE_270)
                elif orientation == 8:
                    im = im.transpose(Image.ROTATE_90)

    # scale it.
    (w, h) = im.size
    r = limit * 1.0 / max(w, h)
    if r < 1.0:
        im = im.resize((int(w * r), int(r * h)))
    im.save(output_path)
    im.close()
