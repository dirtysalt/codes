#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def subseq(a, b):
            n = len(a)
            m = len(b)
            if n == m and a == b:
                return True
            i = 0
            for j in range(m):
                if a[i] == b[j]:
                    i += 1
                    if i == n:
                        break
            return i == n

        def cmp_fn(x, y):
            if len(x) == len(y):
                return -1 if x > y else 0
            return -1 if len(x) > len(y) else 0

        strs.sort(key=functools.cmp_to_key(cmp_fn))
        for i in range(len(strs)):
            if i > 0 and strs[i] == strs[i - 1]:
                continue
            if (i < (len(strs) - 1)) and strs[i] == strs[i + 1]:
                continue
            ok = True
            for j in range(0, i):
                if subseq(strs[i], strs[j]):
                    ok = False
                    break
            if ok:
                print(strs[i])
                return len(strs[i])
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLUSlength(['abf', "aba", "cdc", 'acbcdc', 'acbcdc']))
