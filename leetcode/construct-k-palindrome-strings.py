#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        odd = 0
        pair = 0
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd += 1
            pair += cnt[i] // 2

        print(pair, odd)

        if odd > k:
            return False
        return True
