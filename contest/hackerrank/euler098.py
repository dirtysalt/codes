#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def run(n):
    k = int((10 ** (n - 1)) ** 0.5)
    from collections import Counter
    cnt = Counter()

    def get_ft(x, n):
        bits = [0] * 10
        while x:
            bits[x % 10] += 1
            x = x // 10
        if sum(bits) != n:
            return None
        return tuple(bits)

    ans = 0
    max_cnt = 0
    for i in range(k, 1 << 30):
        k2 = i * i
        if k2 > 10 ** n:
            break
        ft = get_ft(k2, n)
        if not ft:
            continue
        cnt[ft] += 1
        if cnt[ft] >= max_cnt:
            ans = i * i
            max_cnt = cnt[ft]

    return ans


def precompute():
    res = {}
    for n in range(1, 14):
        x = run(n)
        res[n] = x
        print(n, x)
    print(res)


def run2(n):
    d = {1: 9, 2: 81, 3: 961, 4: 9216, 5: 96100, 6: 501264, 7: 9610000, 8: 73462041, 9: 923187456, 10: 9814072356,
         11: 98310467025, 12: 985203145476, 13: 9831140766225}
    return d[n]


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

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    n = read_int()
    ans = run2(n)
    print(ans)


if __name__ == '__main__':
    main()
