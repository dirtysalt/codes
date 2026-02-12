#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dictIndex = {}
        dictData = []
        for s in original + changed:
            if s not in dictIndex:
                dictIndex[s] = len(dictData)
                dictData.append(s)

        INF = 1 << 63
        n = len(dictData)
        C = [[INF] * n for _ in range(n)]
        for i in range(len(original)):
            a, b, c = original[i], changed[i], cost[i]
            a, b = dictIndex[a], dictIndex[b]
            C[a][b] = min(C[a][b], c)

        # only same length strings can transform to each other.
        for t in range(n):
            opts = []
            for i in range(n):
                if len(dictData[i]) == len(dictData[t]):
                    opts.append(i)
            for i in opts:
                for j in opts:
                    C[i][j] = min(C[i][j], C[i][t] + C[t][j])

        # trie structure to avoid long string search.
        class Trie:
            def __init__(self):
                self.child = [None] * 26
                self.index = -1

            def insert(self, s, index):
                t = self
                for c in s:
                    d = ord(c) - ord('a')
                    if not t.child[d]:
                        t2 = Trie()
                        t.child[d] = t2
                    t = t.child[d]
                t.index = index

            def move(self, c):
                d = ord(c) - ord('a')
                return self.child[d]

        root = Trie()
        for i in range(len(dictData)):
            s = dictData[i]
            root.insert(s, i)

        N = len(source)
        dp = [0] * (N + 1)
        for i in reversed(range(N)):
            same = True
            r = INF
            a, b = root, root
            for j in range(i, N):
                same = same & (source[j] == target[j])
                if a and b:
                    a, b = a.move(source[j]), b.move(target[j])
                if same:
                    r = min(r, dp[j + 1])
                elif not (a and b):
                    break
                elif a.index != -1 and b.index != -1:
                    ta, tb = a.index, b.index
                    c = C[ta][tb]
                    r = min(r, c + dp[j + 1])
            dp[i] = r

        ans = dp[0]
        if ans == INF:
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                              changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20], res=28),
    aatest_helper.OrderedDict(source="abcdefgh", target="acdeeghh", original=["bcd", "fgh", "thh"],
                              changed=["cde", "thh", "ghh"], cost=[1, 3, 5], res=9),
    aatest_helper.OrderedDict(source="abcdefgh", target="addddddd", original=["bcd", "defgh"], changed=["ddd", "ddddd"],
                              cost=[100, 1578], res=-1),
]

cases += aatest_helper.read_cases_from_file("tmp.in", 6)

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
