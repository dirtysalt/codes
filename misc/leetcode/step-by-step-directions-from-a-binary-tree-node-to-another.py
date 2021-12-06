#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findPath(root, path, ctx):
            if root is None:
                return
            global pa, pb
            if root.val == startValue:
                ctx[0] = path.copy()

            if root.val == destValue:
                ctx[1] = path.copy()

            path.append(('L', root.val))
            findPath(root.left, path, ctx)
            path.pop()

            path.append(('R', root.val))
            findPath(root.right, path, ctx)
            path.pop()

        ctx = [None, None]
        findPath(root, [], ctx)
        pa, pb = ctx
        # print(pa, pb)

        # check start value up
        for i in reversed(range(len(pa))):
            if pa[i][1] == destValue:
                ans = ['U'] * (len(pa) - i)
                return ''.join(ans)

        pos = {}
        for i in reversed(range(len(pb))):
            pos[pb[i][1]] = i

        ans = []
        if startValue in pos:
            p = pos[startValue]
            ans.extend([x[0] for x in pb[p:]])
        else:
            for i in reversed(range(len(pa))):
                ans.append('U')
                if pa[i][1] in pos:
                    p = pos[pa[i][1]]
                    ans.extend([x[0] for x in pb[p:]])
                    break
        return ''.join(ans)


if __name__ == '__main__':
    pass
