#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        # print(candidates)
        def dfs(i, t, path):
            # print(i, t, path)
            if i == n:
                if t == 0:
                    ans.append(path.copy())
                return

            x = candidates[i]
            j = i
            while j < n and candidates[j] == x:
                j += 1

            c = 0
            for k in range(i, j):
                if t < x:
                    break
                t -= x
                c += 1
                path.append(x)
                dfs(j, t, path)

            for k in range(c):
                path.pop()
                t += x

            dfs(j, t, path)
            return

        dfs(0, target, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))
