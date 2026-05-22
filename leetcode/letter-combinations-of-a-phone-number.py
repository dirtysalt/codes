#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        cm = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for d in digits:
            res2 = []
            for c in cm[int(d)]:
                res2.extend([x + c for x in res])
            res = res2
        ans = res
        ans.sort()
        return ans


cases = [
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().letterCombinations, cases)
