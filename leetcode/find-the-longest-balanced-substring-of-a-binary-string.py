#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                sz = j - i
                if (j + sz) <= n:
                    # s[i:j]
                    # s[j:j+sz]
                    # print(s[i:j], s[j:j+sz])
                    if all((x == '0' for x in s[i:j])) and all((x == '1' for x in s[j:j + sz])):
                        ans = max(ans, 2 * sz)
        return ans


if __name__ == '__main__':
    pass
