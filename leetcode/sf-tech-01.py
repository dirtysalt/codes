#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def hasCycle(self, graph: str) -> bool:
        ps = graph.split(',')
        from collections import defaultdict
        adj = defaultdict(list)
        for p in ps:
            a, b = p.split('->')
            a, b = int(a), int(b)
            adj[a].append(b)

        def visit(p):
            mask = set()

            def dfs(x):
                if x in mask:
                    return True
                mask.add(x)
                if x in adj:
                    for y in adj[x]:
                        if dfs(y): return True
                mask.remove(x)
                return False

            return dfs(p)

        for p in adj:
            if visit(p):
                return True
        return False


true, false, null = True, False, None
cases = [
    ("1->2,2->3,3->1", true),
    ("1->4,2->5,3->6,3->7,4->8,5->8,5->9,6->9,6->11,7->11,8->12,9->12,9->13,10->13,10->14,11->10,11->14", false),
    ("1->4,2->5,3->6,3->7,4->8,5->8,5->9,6->9,6->11,7->11,8->12,9->12,9->13,10->6,10->13,10->14,11->10,11->14", true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().hasCycle, cases)

if __name__ == '__main__':
    pass
