#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        res = []
        res.append(('(', 1))
        n = 2 * n - 1  # left characters.
        while n:
            res2 = []
            for (s, st) in res:
                if (n - st - 2) >= 0:
                    res2.append((s + '(', st + 1))
                if st > 0:
                    res2.append((s + ')', st - 1))
            res = res2
            n -= 1
        return [x[0] for x in res]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(5))
