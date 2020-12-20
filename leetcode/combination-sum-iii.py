#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def __init__(self):
        self.cache = {}

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        cache = self.cache

        def dfs(start, k, n):
            if n == 0 and k == 0:
                return [[]]
            elif n == 0 or k == 0:
                return []
            elif start == 10 or (start * k) > n:
                return []

            key = '{}.{}.{}'.format(start, k, n)
            if key in cache:
                return cache[key]

            res = []

            subs = dfs(start + 1, k, n)
            res.extend(subs)

            subs = dfs(start + 1, k - 1, n - start)
            for sub in subs:
                res.append([start] + sub)
            cache[key] = res

            # print(key, res)
            return res

        ans = dfs(1, k, n)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 10))
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
