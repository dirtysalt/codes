#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        dp = [[] for _ in range(N + 1)]
        dp[0] = []
        dp[1] = [TreeNode(0)]
        for i in range(2, N + 1):
            ans = []
            for j in range(1, i):
                ls = dp[j]
                rs = dp[i - j - 1]
                if not (ls and rs):
                    continue
                for l in ls:
                    for r in rs:
                        t = TreeNode(0)
                        t.left = l
                        t.right = r
                        ans.append(t)
            dp[i] = ans
        return dp[N]
