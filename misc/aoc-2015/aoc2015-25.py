#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def gen_seq(n, x=20151125):
    r = 1
    i, j = 1, 1
    for _ in range(n):
        yield i, j, x
        x = (x * 252533) % 33554393
        i, j = i - 1, j + 1
        if i == 0:
            r += 1
            i, j = r, 1


def main():
    end = (3010, 3019)
    num = 100 * 1000 * 1000
    for i, j, x in gen_seq(num):
        if (i, j) == end:
            print(x)
            break


if __name__ == '__main__':
    main()
