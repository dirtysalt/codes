#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = [[0] * 3 for _ in range(10)]
        for i in range(0, len(rings), 2):
            pos = int(rings[i + 1])
            color = 0
            if rings[i] == 'G':
                color = 1
            elif rings[i] == 'B':
                color = 2
            cnt[pos][color] += 1

        ans = 0
        for i in range(10):
            ok = True
            for j in range(3):
                if cnt[i][j] == 0:
                    ok = False
            if ok:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
