#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def uniqueLetterString(self, S: str) -> int:
#         def chr2idx(c):
#             return ord(c) - ord('A')
#
#         MOD = 10 ** 9 + 7
#         res = 0
#         for i in range(len(S)):
#
#             state = [0] * 26
#             occ = 0
#             for j in range(i, -1, -1):
#                 idx = chr2idx(S[j])
#                 if state[idx] == 0:
#                     occ += 1
#                     state[idx] = 1
#                 elif state[idx] == 1:
#                     occ -= 1
#                     state[idx] = 2
#                 res += occ
#                 res = res % MOD
#         return res

"""
这题目思路应该着重在，某个字符出现了多少次。
假设字符串 AXXXAXXXA，A出现在这些位置上，
0 4 8
那么我们考虑出现在0位置的A，会被计算多少次，应该是(0-(-1)) * (4-0) = 4
同理考虑出现在4位置的A会被计算多少次，应该是4 * (8-4)= 16
8出现的次数有1 * 4 = 4
所以A这个字符总共出现4 + 16 + 4 = 24
"""


class Solution:
    def uniqueLetterString(self, S: str) -> int:
        def chr2idx(c):
            return ord(c) - ord('A')

        dist = [-1] * 26
        for i in range(26):
            dist[i] = [-1]

        for i in range(len(S)):
            idx = chr2idx(S[i])
            dist[idx].append(i)

        for i in range(26):
            dist[i].append(len(S))

        MOD = 10 ** 9 + 7
        res = 0
        for i in range(26):
            size = len(dist[i])
            for j in range(1, size - 1):
                a = dist[i][j - 1]
                b = dist[i][j]
                c = dist[i][j + 1]
                res += (b - a) * (c - b)
                res = res % MOD
        return res


class Solution:
    def uniqueLetterString(self, S: str) -> int:
        def chr2idx(c):
            return ord(c) - ord('A')

        dist = [-1] * 26

        MOD = 10 ** 9 + 7
        res = 0
        n = len(S)

        for i in range(26):
            dist[i] = (-1, -1)

        for i in range(n):
            idx = chr2idx(S[i])
            (a, b) = dist[idx]
            res += (b - a) * (i - b)
            res %= MOD
            dist[idx] = (b, i)

        for i in range(26):
            (a, b) = dist[i]
            res += (b - a) * (n - b)
            res %= MOD
        return res


def test():
    cases = [
        ("ABC", 10),
        ("ABA", 8),
        ("ABABABAB", 28)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (S, exp) = c
        res = sol.uniqueLetterString(S)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
