#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def run(arr):
    ans = 0
    inf = 10 ** 9
    for mx in range(0, 31):
        cur = 0
        best = 0
        for x in arr:
            cur += -inf if x > mx else x
            best = min(cur, best)
            ans = max(ans, (cur - best) - mx)
    return ans


# this is codeforces main function
def main():
    from sys import stdin
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    n = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]
    ans = run(arr)
    print(ans)


if __name__ == '__main__':
    main()
