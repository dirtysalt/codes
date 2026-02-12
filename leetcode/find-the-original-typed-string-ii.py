#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        C = []
        rep = 1
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                C.append(rep)
                rep = 1
            else:
                rep += 1
        C.append(rep)

        MOD = 10 ** 9 + 7
        total = 1
        for c in C:
            total = (total * c) % MOD

        step = min(len(C), k)
        dp = [[0] * k for _ in range(step + 1)]
        dp[0][0] = 1
        # dp[i][j] 处理到 i group时候， 长度为 j 的数量
        # 只处理 <k 的数量，因为每个group至少选择一个，所以长度限制在 min(len(C), k) 上
        # dp[i+1][j+c] += dp[i][j] c = 1..C[i]
        for i in range(step):
            value = 0
            for j in range(k):
                dp[i + 1][j] += value
                value += dp[i][j]
                if j >= C[i]:
                    value -= dp[i][j - C[i]]

        res = sum(dp[-1])
        return (total - res + MOD) % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ("aabbccdd", 7, 5),
    ("aabbccdd", 8, 1),
    ("aaabbb", 3, 8),
    ("aaa", 3, 1),
    ("bbbbbyyyyyyyyyyccccccccyyyqqqqhffffhhhhhhhhsswwwwvvvvvlllldddddddddnnnnnnvr", 69, 23761),
]

aatest_helper.run_test_cases(Solution().possibleStringCount, cases)

if __name__ == '__main__':
    pass
