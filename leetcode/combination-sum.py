#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         candidates = [x for x in candidates if x <= target]
#         if not candidates: return []
#
#         candidates.sort()
#         st = []
#         for i in range(len(candidates)):
#             sub_st = []
#             for j in range(0, target + 1):
#                 sub_st.append([])
#             st.append(sub_st)
#
#         a = candidates[0]
#         c = 0
#         while (a * c) <= target:
#             st[0][a * c].append([a] * c)
#             c += 1
#
#         for i in range(1, len(candidates)):
#             a = candidates[i]
#             for t in range(0, target + 1):
#                 c = 0
#                 while (a * c) <= t:
#                     rest = t - a * c
#                     possibles = st[i - 1][rest]
#                     for p in possibles:
#                         st[i][t].append(p + [a] * c)
#                     c += 1
#
#         return st[len(candidates) - 1][target]


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        cache = {}
        candidates.sort()

        def solve(idx, target):
            if target == 0:
                return [[]]
            if idx < 0:
                return []
            cache_key = '{}.{}'.format(idx, target)
            if cache_key in cache:
                return cache[cache_key]
            res = []
            if candidates[idx] <= target:
                xs = solve(idx, target - candidates[idx])
                for x in xs:
                    y = x + [candidates[idx]]
                    res.append(y)
            xs = solve(idx - 1, target)
            res.extend(xs)
            cache[cache_key] = res
            return res

        res = solve(len(candidates) - 1, target)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))
