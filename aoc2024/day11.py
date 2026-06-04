#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(nums):
    def trans(x):
        if x == 0: return [1]
        s = str(x)
        if len(s) % 2 == 0:
            n = len(s) // 2
            return [int(s[:n]), int(s[n:])]
        return [x * 2024]

    for _ in range(25):
        tmp = []
        for x in nums:
            tmp.extend(trans(x))
        nums = tmp

    return len(nums)


def main():
    input = 'tmp.in'
    with open(input) as fh:
        for s in fh:
            nums = [int(x) for x in s.split()]
            print(solve(nums))


if __name__ == '__main__':
    main()
