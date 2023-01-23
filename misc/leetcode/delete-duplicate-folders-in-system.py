#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Trie:
    def __init__(self, w, hv):
        self.w = w
        self.hv = hv
        self.delete = False
        self.child = {}
        self.child_hv = 0


def insert_trie(root, path):
    for w in path:
        hv = hash(w)
        if hv not in root.child:
            t = Trie(w, hv)
            root.child[hv] = t
        else:
            t = root.child[hv]
        root = t


MUL = 31


def update_hash(root, hash_values):
    child_hv = 0
    if root.child:
        for c in root.child.values():
            hv = update_hash(c, hash_values)
            child_hv = child_hv * MUL + hv
        hash_values[child_hv] += 1
        root.child_hv = child_hv
    hv = child_hv * MUL + root.hv
    return hv


def mark_delete(root, hash_values):
    if hash_values[root.child_hv] > 1:
        root.delete = True
        return
    for c in root.child.values():
        mark_delete(c, hash_values)
    return


def visit_output(root, trace, output):
    if root.delete:
        return

    trace.append(root.w)
    output.append(trace.copy())
    for c in root.child.values():
        visit_output(c, trace, output)
    trace.pop()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        t = Trie('zz', hash('zz'))
        for path in paths:
            insert_trie(t, path)
        from collections import Counter
        hash_values = Counter()
        update_hash(t, hash_values)
        # print(hash_values)
        mark_delete(t, hash_values)

        ans = []
        trace = []
        visit_output(t, trace, ans)

        for comp in ans:
            comp.pop(0)
        ans.pop(0)
        return ans


true, false, null = True, False, None
cases = [
    ([["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]], [["d"], ["d", "a"]]),
    ([["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]],
     [["c"], ["c", "b"], ["a"], ["a", "b"]]),
    ([["a", "b"], ["c", "d"], ["c"], ["a"]], [["c"], ["c", "d"], ["a"], ["a", "b"]]),
    ([["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"]], []),
    ([["a"], ["a", "x"], ["a", "x", "y"], ["a", "z"], ["b"], ["b", "x"], ["b", "x", "y"], ["b", "z"], ["b", "w"]],
     [["b"], ["b", "w"], ["b", "z"], ["a"], ["a", "z"]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().deleteDuplicateFolder, cases)

if __name__ == '__main__':
    pass
