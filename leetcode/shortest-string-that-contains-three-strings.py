#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(a, b):
            rs = []
            if a.find(b) != -1:
                rs.append(a)
            rs.append(a + b)

            index = set()
            for i in range(len(b)):
                index.add(b[:i + 1])

            for i in range(len(a)):
                if a[i:] in index:
                    rs.append(a + b[len(a) - i:])
            return rs

        def merge2(a, b, c):
            rs = merge(a, b)
            rs.extend(merge(b, a))
            rs2 = []
            for r in rs:
                rs2.extend(merge(r, c))
                rs2.extend(merge(c, r))
            return rs2

        res = []
        res.extend(merge2(a, b, c))
        res.extend(merge2(a, c, b))
        res.extend(merge2(b, c, a))
        sz = min([len(x) for x in res])
        return min([x for x in res if len(x) == sz])


true, false, null = True, False, None
import aatest_helper

cases = [
    ("abc", "bca", "aaa", "aaabca"),
    ("ab", "ba", "aba", "aba")
]

aatest_helper.run_test_cases(Solution().minimumString, cases)

if __name__ == '__main__':
    pass
