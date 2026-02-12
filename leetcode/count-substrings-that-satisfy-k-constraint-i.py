#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + (s[i] == '1')

        ans = 0
        for sz in range(1, n + 1):
            for i in range(0, n - sz + 1):
                end = i + sz - 1
                one = acc[end + 1] - acc[i]
                if one <= k or (sz - one) <= k:
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
