#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(exp, nums):
    def dfs(now, i):
        if i == len(nums):
            return now == exp
        x = nums[i]
        if dfs(now + x, i + 1):
            return True
        if dfs(now * x, i + 1):
            return True
        return False

    ok = dfs(nums[0], 1)
    return exp if ok else 0


def main():
    input = 'tmp.in'
    ans = 0
    with open(input) as fh:
        for s in fh:
            exp, nums = s.split(':')
            exp = int(exp)
            nums = [int(x) for x in nums.split()]
            ans += solve(exp, nums)

    print(ans)


if __name__ == '__main__':
    main()
