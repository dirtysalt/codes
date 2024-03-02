#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
import itertools


def test(nums, size):
    dp = [0] * (size + 1)
    dp[0] = 1
    for x in nums:
        for i in range(0, size):
            if dp[i] == 0: continue
            if (i + x) <= size:
                dp[i + x] += 1
    return dp[size] != 0


def solve(nums, size):
    INF = 1 << 63
    ans = INF
    for sz in range(1, len(nums) - 1):
        for seq in itertools.combinations(nums, sz):
            if sum(seq) != size: continue
            from collections import Counter
            c = Counter(seq)
            rest = []
            for x in nums:
                if c[x] > 0:
                    c[x] -= 1
                else:
                    rest.append(x)
            if test(rest, size):
                r = functools.reduce(lambda x, y: x * y, seq)
                print(seq, '--->', r)
                ans = min(ans, r)
        if ans != INF:
            print(ans)
            break


def main():
    test = False
    # test = True

    if test:
        nums = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
    else:
        with open('input.txt') as fh:
            nums = [int(x) for x in fh]
    print(nums)
    nums.sort()
    s = sum(nums)
    solve(nums, s // 3)


if __name__ == '__main__':
    main()
