#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # 主要特点就是上下两个部分只会在对角线有交集，所以可以分别针对上下两个部分进行求解，
        # 但是需要忽略对角线的部分，因为对角线部分可以被中间部分所占有
        import functools
        @functools.lru_cache(None)
        def dfs(x, y, t, upper):
            if t == (n - 1):
                if (x, y) == (n - 1, n - 1):
                    return 0
                return -1

            extra = (n - 1 - t)
            if x + extra < (n - 1) or x >= n:
                return -1
            if y + extra < (n - 1) or y >= n:
                return -1

            curr = (fruits[x][y] if (x != y) else 0)

            def next(x, y):
                if upper:
                    for dy in (-1, 0, 1):
                        yield x + 1, y + dy
                else:
                    for dx in (-1, 0, 1):
                        yield x + dx, y + 1

            res = -1
            for x2, y2 in next(x, y):
                r = dfs(x2, y2, t + 1, upper)
                if r == -1: continue
                res = max(res, curr + r)
            return res

        upper = dfs(0, n - 1, 0, True)
        lower = dfs(n - 1, 0, 0, False)
        dfs.cache_clear()
        ans = upper + lower
        for i in range(0, n):
            ans += fruits[i][i]

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]], 100),
    ([[1, 1], [1, 1]], 4),
]
# cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().maxCollectedFruits, cases)

if __name__ == '__main__':
    pass
