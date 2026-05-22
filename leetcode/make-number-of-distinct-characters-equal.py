#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        def Count(w):
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            return cnt

        cnt1 = Count(word1)
        cnt2 = Count(word2)

        def check(a, b):
            x, y = 0, 0
            for i in range(26):
                if a[i] > 0: x += 1
                if b[i] > 0: y += 1
            return x == y

        for i in range(26):
            if cnt1[i] == 0: continue
            for j in range(26):
                if cnt2[j] == 0: continue
                cnt1[i] -= 1
                cnt1[j] += 1
                cnt2[j] -= 1
                cnt2[i] += 1
                if check(cnt1, cnt2): return True
                cnt1[i] += 1
                cnt1[j] -= 1
                cnt2[i] -= 1
                cnt2[j] += 1
        return False


if __name__ == '__main__':
    pass
