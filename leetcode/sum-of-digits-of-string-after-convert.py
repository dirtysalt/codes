#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0

        for c in s:
            x = ord(c) - ord('a') + 1
            while x:
                ans += x % 10
                x = x // 10

        for _ in range(k - 1):
            tmp = 0
            while ans:
                tmp += ans % 10
                ans = ans // 10
            ans = tmp

        return ans


if __name__ == '__main__':
    pass
