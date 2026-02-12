#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def cmp(a, b):
            if len(a) != len(b):
                return False

            cnt = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1

            return cnt <= 2

        ans = []
        for q in queries:
            for d in dictionary:
                if cmp(q, d):
                    ans.append(q)
                    break
        return ans


if __name__ == '__main__':
    pass
