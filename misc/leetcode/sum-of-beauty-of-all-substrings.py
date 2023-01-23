#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def beautySum(self, s: str) -> int:
        class HT:
            def __init__(self, n, cmp):
                sz = 1
                while sz < n:
                    sz = sz * 2
                self.sz = sz
                self.data = [0] * (2 * sz)
                self.cmp = cmp

            def update(self, i, x):
                self.data[i + self.sz] = x
                idx = i + self.sz
                while idx != 1:
                    p = idx // 2
                    x = self.data[2 * p]
                    y = self.data[2 * p + 1]
                    if self.cmp(x, y):
                        self.data[p] = x
                    else:
                        self.data[p] = y
                    idx = p

            def top(self):
                return self.data[1]

        n = len(s)
        ans = 0

        def cmp(x, y):
            if x == 0: return False
            if y == 0: return True
            return x < y

        for i in range(n):
            MinH = HT(26, cmp)
            MaxH = HT(26, lambda x, y: x > y)
            freq = [0] * 26
            for j in range(i, n):
                c = ord(s[j]) - ord('a')
                freq[c] += 1
                MinH.update(c, freq[c])
                MaxH.update(c, freq[c])
                # print(MaxH.top(), MinH.top(), s[i:j + 1])
                delta = MaxH.top() - MinH.top()
                ans += delta
        return ans


cases = [
    ("aabcb", 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().beautySum, cases)
