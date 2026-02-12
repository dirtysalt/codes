#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)

        from collections import Counter
        cnt = Counter()
        rep, sz = 0, n // k
        for i in range(sz):
            s = word[i * k: i * k + k]
            cnt[s] += 1
            rep = max(rep, cnt[s])

        return sz - rep


if __name__ == '__main__':
    pass
