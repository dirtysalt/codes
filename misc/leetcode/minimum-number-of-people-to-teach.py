#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        FS = []
        LS = [set(x) for x in languages]
        for x, y in friendships:
            if not (LS[x-1] & LS[y-1]):
                FS.append((x-1, y-1))

        ans = len(languages)
        for L in range(1, n+1):
            cnt = 0
            LS = [set(x) for x in languages]
            for x, y in FS:
                if not (LS[x] & LS[y]):
                    if L not in LS[x]:
                        cnt += 1
                    if L not in LS[y]:
                        cnt += 1
                    LS[x].add(L)
                    LS[y].add(L)
            ans = min(ans, cnt)

        return ans

import aatest_helper

cases = [
    ( 2, [[1],[2],[1,2]],  [[1,2],[1,3],[2,3]], 1),
    ( 3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]], 2)
]

aatest_helper.run_test_cases(Solution().minimumTeachings, cases)
