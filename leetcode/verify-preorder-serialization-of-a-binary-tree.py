#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def end(self, t):
        if self.left is None:
            self.left = t
            return True

        if self.right is None:
            self.right = t
            return True

        return False

    def full(self):
        return self.left and self.right


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        preorder = preorder.split(',')
        if preorder == ['#']:
            return True

        st = []
        for c in preorder:
            if c == '#':
                if not st:
                    return False
                p = st[-1]
                if not p.end('#'):
                    return False
            else:
                t = TreeNode(c)
                st.append(t)

            # compact stack
            while len(st) >= 2:
                p0 = st[-1]
                p1 = st[-2]
                if p1.full():
                    return False

                if p0.full():
                    p1.end(p0)
                    st.pop()
                else:
                    break

        if len(st) == 1 and st[0].full():
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print((s.isValidSerialization(preorder)))
