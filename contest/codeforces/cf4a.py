#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(w):
    if w % 2 == 0 and w > 2:
        print('YES')
    else:
        print('NO')


def main():
    w = int(stdin.readline())
    run(w)


if __name__ == '__main__':
    main()
