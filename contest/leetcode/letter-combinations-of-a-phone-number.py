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
        dm = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for i in range(len(digits) - 1, -1, -1):
            d = int(digits[i])
            s = dm[d]
            res2 = []
            for c in s:
                for r in res:
                    res2.append(c + r)
            res = res2
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
