#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Tree:
    def __init__(self, index):
        self.child = []
        self.index = index
        self.size = 0
        self.sub_score = 0
        self.score = 0

    def add(self, c):
        self.child.append(c)

    def __repr__(self):
        return 'Tree(index=%d, size=%d, sub_score=%d, score=%d)' % (self.index, self.size, self.sub_score, self.score)


def compute_size(root, n):
    size = 1
    sub_score = 1
    for c in root.child:
        sz = compute_size(c, n)
        size += sz
        sub_score *= sz
    root.sub_score = sub_score
    root.size = size

    if root.size == n:
        root.score = root.sub_score
    else:
        root.score = (n - root.size) * root.sub_score
    return size


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        trees = [Tree(index) for index in range(n)]
        root = None
        for i in range(n):
            p = parents[i]
            if p == -1:
                root = trees[i]
                continue
            trees[p].add(trees[i])

        compute_size(root, n)
        max_score = max((t.score for t in trees))
        ans = 0
        for t in trees:
            if t.score == max_score:
                ans += 1
        return ans


true, false, null = True, False, None
cases = [
    ([-1, 2, 0, 2, 0], 3),
    ([-1, 2, 0], 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countHighestScoreNodes, cases)

if __name__ == '__main__':
    pass
