#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26
        way = [0] * 8
        for c in word:
            cnt[ord(c) - ord('a')] += 1
        cnt.sort(reverse=True)

        ans = 0
        w = 0
        for x in cnt:
            ans += x * (way[w] + 1)
            way[w] += 1
            w = (w + 1) % 8
        return ans


if __name__ == '__main__':
    pass
