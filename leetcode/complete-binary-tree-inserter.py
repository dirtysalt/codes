#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:

    def __init__(self, root: TreeNode):
        def mark(root):
            if root is None:
                return 0

            lc = mark(root.left)
            rc = mark(root.right)
            root.count = 1 + lc + rc
            return root.count

        mark(root)
        self.root = root

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        node.count = 1
        root = self.root

        while True:
            root.count += 1
            if root.left is None:
                root.left = node
                break
            elif root.right is None:
                root.right = node
                break

            lc = root.left.count
            rc = root.right.count
            if (lc & (lc + 1)) != 0:
                root = root.left
            elif (rc & (rc + 1)) != 0:
                root = root.right
            else:
                root = root.left if rc == lc else root.right

        return root.val

    def get_root(self) -> TreeNode:
        return self.root


import aatest_helper
null = None
cases = [
    (["CBTInserter", "insert", "insert", "get_root"],
     [[aatest_helper.list_to_tree([1, 2, 3, 4, 5, 6])], [7], [8], []],
     [null, 3, 4, [1, 2, 3, 4, 5, 6, 7, 8]])
]
aatest_helper.run_simulation_cases(CBTInserter, cases)
