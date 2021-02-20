#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# this is codeforces main function
def main():
    from sys import stdin

    def read_int():
        return int(stdin.readline())

    def read_int_array(sep=None):
        return [int(x) for x in stdin.readline().split(sep)]

    def read_str_array(sep=None):
        return [x.strip() for x in stdin.readline().split(sep)]

    import os

    # if os.path.exists('tmp.in'):
    #     stdin = open('tmp.in')

    n = read_int()
    xs = read_int_array()
    xs.sort()
    ans = ' '.join((str(x) for x in xs))
    print(ans)


if __name__ == '__main__':
    main()