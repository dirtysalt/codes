#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def calculateScore(self, s: str) -> int:
        ss = [ord(x) - ord('a') for x in s]
        from collections import defaultdict
        pos = defaultdict(list)

        ans = 0
        for i in range(len(ss)):
            x = ss[i]
            exp = 25 - x
            if pos[exp]:
                j = pos[exp].pop()
                ans += (i - j)
            else:
                pos[x].append(i)
        return ans


if __name__ == '__main__':
    pass
