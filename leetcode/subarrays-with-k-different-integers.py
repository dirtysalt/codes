#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        from collections import Counter
        cnt = Counter()
        vis = set()

        j = 0
        matched = 0
        ans = 0
        for i in range(len(A)):
            x = A[i]
            vis.add(x)
            cnt[x] += 1

            # 回退窗口到=K的情况
            if len(vis) > K:
                while j <= i:
                    y = A[j]
                    cnt[y] -= 1
                    j += 1
                    if cnt[y] == 0:
                        vis.remove(y)
                        break
                # print('NEXT', i, j, matched)
                assert len(vis) == K
                matched = j

            # 注意这里matched表示最开始满足=K的下标
            # j表示包含当前元素，至少从需要保留到什么下标
            # K=2, [1,2,1,2].
            # i=3时，matched=0, 而j=2
            # 所以包含i=3这个元素时，共有(j-matched+1)=3中可能
            # 【1,2,1,2], [2,1,2], [1,2]
            if len(vis) == K:
                while j <= i:
                    y = A[j]
                    if cnt[y] == 1:
                        break
                    cnt[y] -= 1
                    j += 1

                assert len(vis) == K
                # 当前j..i是满足条件的
                # 有 matched..j个组合
                # print('GOT', i, j, matched)
                ans += (j - matched + 1)

        return ans


cases = [
    ([1, 2, 1, 3, 4], 3, 3),
    ([1, 2, 1, 2, 3], 2, 7),
    ([2, 1, 1, 1, 2], 1, 8),
    ([27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4,
      11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18,
      49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45,
      37, 40, 35, 50, 50, 23, 32, 1, 2], 20, 149),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().subarraysWithKDistinct, cases)
