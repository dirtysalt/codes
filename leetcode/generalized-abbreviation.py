#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     """
#     @param word: the given word
#     @return: the generalized abbreviations of a word
#     """
#
#     def generateAbbreviations(self, word):
#         # Write your code here
#
#         def gen(w):
#             if w == '':
#                 return ['']
#
#             ans = []
#             for i in range(1, len(w) + 1):
#                 s, t = w[:i], w[i:]
#                 c = '%d' % len(s)
#                 res = gen(t)
#                 ans.extend([s + x for x in res if not x or x[0].isdigit()])
#                 ans.extend([c + x for x in res if not (x and x[0].isdigit())])
#             return ans
#
#         ans = gen(word)
#         ans = sorted(ans)
#         return ans

# class Solution:
#     """
#     @param word: the given word
#     @return: the generalized abbreviations of a word
#     """
#
#     def generateAbbreviations(self, word):
#         # Write your code here
#
#         def gen(w):
#             if w == '':
#                 return [''], ['']
#
#             words = []
#             digits = []
#
#             for i in range(1, len(w) + 1):
#                 s, t = w[:i], w[i:]
#                 c = '%d' % len(s)
#                 xs, ys = gen(t)
#                 words.extend([s + x for x in ys])
#                 digits.extend([c + x for x in xs])
#
#             return words, digits
#
#         words, digits = gen(word)
#         ans = words + digits
#         ans = sorted(ans)
#         return ans

class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """

    def generateAbbreviations(self, word):
        # Write your code here

        dp = {}

        def gen(w):
            if w == '':
                return [''], ['']

            if w in dp:
                return dp[w]

            words = []
            digits = []

            for i in range(1, len(w) + 1):
                s, t = w[:i], w[i:]
                c = '%d' % len(s)
                xs, ys = gen(t)
                words.extend([s + x for x in ys])
                digits.extend([c + x for x in xs])

            dp[w] = (words, digits)
            return words, digits

        words, digits = gen(word)
        ans = words + digits
        ans = sorted(ans)
        return ans


cases = [
    ("word",
     sorted(["1o1d", "1o2", "1or1", "1ord", "2r1", "2rd", "3d", "4", "w1r1", "w1rd", "w2d", "w3", "wo1d", "wo2", "wor1",
             "word"]))
]

import aatest_helper

aatest_helper.run_test_cases(Solution().generateAbbreviations, cases)
