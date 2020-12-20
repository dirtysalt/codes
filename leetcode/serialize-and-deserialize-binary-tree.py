#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.ser(root, res)
        return ','.join(map(str, res))

    def ser(self, root, res):
        if root is None:
            res.append('#')
            return
        res.append(root.val)
        self.ser(root.left, res)
        self.ser(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')
        node, idx = self.des(res, 0)
        assert idx == len(res)
        return node

    def des(self, res, idx):
        if res[idx] == '#':
            return None, idx + 1
        val = int(res[idx])
        left, idx = self.des(res, idx + 1)
        right, idx2 = self.des(res, idx)
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node, idx2


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    pass
