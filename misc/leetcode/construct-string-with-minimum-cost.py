#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        INF = 1 << 61

        class Trie:
            def __init__(self):
                self.child = [None] * 26
                self.cost = INF

            def insert(self, s, cost):
                root = self
                for ch in s:
                    c = ord(ch) - ord('a')
                    if root.child[c] is None:
                        root.child[c] = Trie()
                    root = root.child[c]
                root.cost = min(root.cost, cost)

            def match(self, t):
                root = self
                for i in range(len(t)):
                    c = ord(t[i]) - ord('a')
                    if root.child[c] is None:
                        break
                    root = root.child[c]
                    if root.cost != INF:
                        yield t[i + 1:], root.cost

        root = Trie()
        for w, c in zip(words, costs):
            root.insert(w, c)

        import functools
        @functools.cache
        def dfs(i):
            if i == len(target): return 0

            ans = INF
            t = target[i:]
            for t2, cost in root.match(t):
                idx = i + len(t) - len(t2)
                if cost >= ans:
                    continue
                r = dfs(idx) + cost
                ans = min(ans, r)
            return ans

        ans = dfs(0)
        if ans == INF: ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(target="abcdef", words=["abdef", "abc", "d", "def", "ef"], costs=[100, 1, 1, 10, 5],
                              res=7),
    aatest_helper.OrderedDict(target="aaaa", words=["z", "zz", "zzz"], costs=[1, 10, 100], res=-1),
    ("r", ["r", "r", "r", "r"], [1, 6, 3, 3], 1),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 4)

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
