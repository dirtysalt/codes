#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []

        from collections import deque
        dq = deque()
        if root is not None:
            dq.append((root, 0))

        while dq:
            (t, d) = dq.popleft()
            if len(ans) == d:
                ans.append([])
            ans[d].append(t.val)

            for x in t.children:
                if x is None: continue
                dq.append((x, d + 1))
        return ans
