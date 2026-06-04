#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


"""
find_next是找到從某個点i向后看，第一个ch出现在什么位置，然后将这个信息缓存下来。
这样比如在匹配acd, ace的时候，在匹配acd时，我们就可以知道a之后c最先出现在什么位置。
之所以可以这么匹配，是因为这题目本质上是贪心匹配，尽可能地早匹配比晚匹配要好。
"""


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        cache = {}
        n = len(S)

        def find_next(i, ch):
            key = '{}.{}'.format(i, ch)
            if key in cache:
                return cache[key]

            ans = n
            for j in range(i, n):
                if S[j] == ch:
                    ans = j
                    break
            cache[key] = ans
            return ans

        ans = 0
        for w in words:
            i = 0
            matched = True
            for ch in w:
                j = find_next(i, ch)
                if j == n:
                    matched = False
                    break
                i = j + 1
            if matched:
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numMatchingSubseq('abcde', ["a", "bb", "acd", "ace"]))
