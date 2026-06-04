#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            cnt[i] += 1

        MOD = 10 ** 9 + 7
        for _ in range(t):
            cnt2 = [0] * 26
            for k in range(25):
                cnt2[k + 1] += cnt[k]
            cnt2[0] += cnt[-1]
            cnt2[1] += cnt[-1]
            for k in range(26):
                cnt2[k] %= MOD
            cnt = cnt2

        return sum(cnt) % MOD


if __name__ == '__main__':
    pass
