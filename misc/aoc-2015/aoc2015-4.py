#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import hashlib


def find(header):
    x = -1
    while True:
        x += 1
        s = header + str(x)
        if hashlib.md5(s.encode('utf-8')).hexdigest().startswith('00000'):
            print(x)
            break


def main():
    find('iwrupvqb')


if __name__ == '__main__':
    main()
