#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 1 << 30
        C = [[INF] * 26 for _ in range(26)]

        def to_int(c):
            return ord(c) - ord('a')

        for i in range(len(original)):
            a = to_int(original[i])
            b = to_int(changed[i])
            c = cost[i]
            C[a][b] = min(C[a][b], c)

        for t in range(26):
            for i in range(26):
                for j in range(26):
                    C[i][j] = min(C[i][j], C[i][t] + C[t][j])

        ans = 0
        for s, t in zip(source, target):
            a, b = to_int(s), to_int(t)
            if a == b: continue
            if C[a][b] == INF:
                return -1
            ans += C[a][b]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                              changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20], res=28),
    aatest_helper.OrderedDict(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2],
                              res=12),
    aatest_helper.OrderedDict(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000], res=-1),
]

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
