#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [0] * n
        rs = [(i, score[i]) for i in range(n)]
        rs.sort(key=lambda x: -x[1])

        for i in range(n):
            pos = rs[i][0]
            if i < 3:
                if i == 0:
                    ans[pos] = "Gold Medal"
                elif i == 1:
                    ans[pos] = "Silver Medal"
                else:
                    ans[pos] = "Bronze Medal"
            else:
                ans[pos] = str(i + 1)
        return ans


if __name__ == '__main__':
    pass
