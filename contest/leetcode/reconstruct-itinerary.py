#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        edges = defaultdict(list)
        for (idx, (a, b)) in enumerate(tickets):
            edges[a].append((b, idx))
        for xs in edges.values():
            xs.sort()

        ans = []
        visited = set()

        def dfs():
            if len(ans) == (len(tickets) + 1):
                return True

            p = ans[-1]
            for (v, ti) in edges[p]:
                if ti in visited:
                    continue
                visited.add(ti)
                ans.append(v)
                if dfs():
                    return True
                visited.remove(ti)
                ans.pop()
            return False

        ans.append('JFK')
        dfs()
        return ans


cases = [
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
     ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]], ['JFK', 'NRT', 'JFK', 'KUL'])
]
import aatest_helper

aatest_helper.run_test_cases(Solution().findItinerary, cases)
