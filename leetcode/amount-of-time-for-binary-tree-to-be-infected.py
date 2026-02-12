#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def build(root):
            st = [root]
            root.up = None
            begin = None
            while st:
                p = st.pop()
                p.time = -1
                if p.val == start:
                    begin = p
                l, r = p.left, p.right
                if l:
                    l.up = p
                    st.append(l)
                if r:
                    r.up = p
                    st.append(r)
            return begin

        def visit(begin):
            st = [begin]
            begin.time = 0
            ans = 0
            while st:
                p = st.pop()
                rs = [p.up, p.left, p.right]
                for r in rs:
                    if r and r.time == -1:
                        r.time = p.time + 1
                        ans = max(ans, r.time)
                        st.append(r)
            return ans

        begin = build(root)
        ans = visit(begin)
        return ans


if __name__ == '__main__':
    pass
