#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import argparse
import cgi

import numpy
from PIL import Image
from moviepy.editor import *


def mosaic_effect(im, box, scale=0.2):
    im2 = im.crop(box)
    sz = im2.size
    im2 = im2.resize((int(im2.size[0] * scale), int(im2.size[1] * scale)), Image.NEAREST)
    im2 = im2.resize(sz)
    im3 = im.copy()
    im3.paste(im2, box)
    return im3


def test_image_effect():
    for f in ('sample.jpg', 'sample.png'):
        rim = Image.open(f).convert('RGB')
        sz = rim.size
        im3 = mosaic_effect(rim, (sz[0] / 4, sz[1] / 4, sz[1] * 3 / 4, sz[1] * 3 / 4), 0.05)
        im3.save('mosaic-%s' % (f))


def process_clip(clip_name):
    clip = VideoFileClip(clip_name)

    def make_frame(t):
        f = clip.get_frame(t)
        (h, w, _) = f.shape
        im = Image.fromarray(f)
        im = mosaic_effect(im, (40, 40, 600, 600), scale=0.05)
        f2 = numpy.asarray(im)  # much more efficient than numpy.array(im.getdata())
        f2 = f2.reshape((im.size[1], im.size[0], 3))
        return f2

    clip2 = VideoClip(make_frame, duration=clip.duration)
    clip2.write_videofile(clip_name + '.mp4', fps=clip.fps)
    clip = VideoFileClip(clip_name).fx(vfx.mirror_x)
    clip.write_videofile(clip_name + '.mirror.mp4', fps=clip.fps)


# greyscale_10 = " .:-=+*#%@"
# def image2ascii(im, constrast = False):
#     im = im.convert("L") # convert to mono
#     ss = []
#     idx = 0
#     for y in range(0,im.size[1]):
#         s = ''
#         for x in range(0,im.size[0]):
#             p = 255 - im.getpixel((x, y))
#             if constrast: p = 255 - p
#             if p >= 225: c = greyscale_10[-1]
#             else: c = greyscale_10[p / 25]
#             s = s + c
#         ss.append(s)
#     return ss

greyscale_70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.."


def image2ascii(im, contrast=False):
    im = im.convert("L")  # convert to mono
    ss = []
    idx = 0
    for y in range(0, im.size[1]):
        s = ''
        for x in range(0, im.size[0]):
            p = im.getpixel((x, y))
            if contrast: p = 255 - p
            if p >= 207:
                c = greyscale_70[-1]
            else:
                c = greyscale_70[p / 3]
            s = s + c
        ss.append(s)
    return ss


def gen_font_string(im, ss):
    (w, h) = im.size
    ys = []
    for y in range(h):
        sp = None
        sp_idx = -1
        xs = []
        for x in range(w):
            p = im.getpixel((x, y))
            if p == sp:
                continue
            elif sp:
                xs.append((sp, sp_idx, x))
            sp = p
            sp_idx = x
        if sp: xs.append((sp, sp_idx, w))
        s = ''.join(
            ["<font color=\"#%X%X%X\">%s</font>" % (sp[0], sp[1], sp[2], cgi.escape(ss[y][f:t])) for (sp, f, t) in
             xs])
        ys.append(s)
    s = '</br>\n'.join(ys)
    return s


with open('image.temp') as fh:
    html_template = fh.read()


def image2html(im, contrast=True, font_color=False):
    color = 'white' if contrast else 'black'
    bcolor = 'black' if contrast else 'white'
    ss = image2ascii(im, contrast=contrast)
    if not font_color:
        image = '</br>\n'.join([cgi.escape(x) for x in ss])
    else:
        image = gen_font_string(im, ss)
    return html_template % (locals())


def test_image_to_html():
    width = 80
    for f in ('sample.jpg', 'sample.png'):
        output_file = 'ascii-' + f + '.html'
        image_to_html(f, output_file, width)


def image_to_html(input_file, output_file, width):
    rim = Image.open(input_file).convert('RGB')
    im = rim.resize((width, int(rim.size[1] * width / rim.size[0])))
    html = image2html(im, contrast=True, font_color=True)
    with open(output_file, 'w') as fh:
        fh.write(html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-image-effect', action='store_true')
    parser.add_argument('--test-image-to-html', action='store_true')
    parser.add_argument('--process-clip', action='store_true')
    parser.add_argument('--image-to-html', action='store_true')
    parser.add_argument('--input-file', action='store')
    parser.add_argument('--output-file', action='store')
    parser.add_argument('--width', action='store', type=int, default=80)
    args = parser.parse_args()

    if args.test_image_effect:
        test_image_effect()
    elif args.test_image_to_html:
        test_image_to_html()
    elif args.process_clip:
        process_clip(args.input_file)
    elif args.image_to_html:
        image_to_html(args.input_file, args.output_file, args.width)


if __name__ == '__main__':
    main()
