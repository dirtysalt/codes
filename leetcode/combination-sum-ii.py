#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        dp = {}
        candidates.sort()

        def solve(idx, target):
            if target == 0:
                return [[]]
            if idx < 0:
                return []

            cache_key = '{}.{}'.format(idx, target)
            if cache_key in dp:
                return dp[cache_key]

            res = []
            # 避免选择重复元素
            next_idx = idx - 1
            while next_idx >= 0 and candidates[next_idx] == candidates[idx]:
                next_idx -= 1

            # 选择当前元素的可能性
            if candidates[idx] <= target:
                xs = solve(idx - 1, target - candidates[idx])
                for x in xs:
                    res.append(x + [candidates[idx]])

            # 不选择当前元素可能性
            xs = solve(next_idx, target)
            res.extend(xs)
            dp[cache_key] = res
            return res

        res = solve(len(candidates) - 1, target)
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))
