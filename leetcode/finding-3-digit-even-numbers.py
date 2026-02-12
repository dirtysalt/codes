#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = [0] * 10

        for d in digits:
            cnt[d] += 1

        ans = set()

        def dfs(k, acc):
            if k == 3:
                if acc % 2 == 0:
                    ans.add(acc)
                return

            for i in range(10):
                if k == 0 and i == 0: continue
                if cnt[i] == 0: continue
                cnt[i] -= 1
                dfs(k + 1, acc * 10 + i)
                cnt[i] += 1

        dfs(0, 0)
        ans = list(ans)
        ans.sort()
        return ans


if __name__ == '__main__':
    pass
