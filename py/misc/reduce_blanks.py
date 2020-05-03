#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import sys


def flush_buffers(output, buffers):
    if not buffers: return
    min_indent = min([x.find('-') for x in buffers])
    for x in buffers:
        indent = x.find('-')
        output.append(' ' * (indent - min_indent) + x[indent:])
    buffers.clear()


def reduce_blanks(lines):
    output = []
    buffers = []
    for x in lines:
        y = x
        if x.strip().startswith('-'):
            buffers.append(x)
        else:
            flush_buffers(output, buffers)
            output.append(y)
    flush_buffers(output, buffers)
    return output


def reduce_files(files):
    for f in files:
        print('reduce blanks on {}'.format(f))
        with open(f) as fh:
            output = reduce_blanks(fh)
        with open(f, 'w') as fh:
            fh.writelines(output)


def main():
    files = sys.argv[1:]
    reduce_files(files)


if __name__ == '__main__':
    main()
