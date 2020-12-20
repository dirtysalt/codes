#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def getCount(s):
            cnt = [0] * 26
            for c in s:
                x = ord(c) - ord('a')
                cnt[x] += 1
            return cnt

        cnt1 = getCount(word1)
        cnt2 = getCount(word2)
        # 确保两个字符串拥有同样的字符集合
        for i in range(26):
            if cnt1[i] == 0 and cnt2[i] != 0:
                return False
            if cnt2[i] == 0 and cnt1[i] != 0:
                return False
        cnt1.sort()
        cnt2.sort()
        return cnt1 == cnt2


cases = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
    ("cabbba", "aabbss", False),
    ("uau", "ssx", False),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().closeStrings, cases)
