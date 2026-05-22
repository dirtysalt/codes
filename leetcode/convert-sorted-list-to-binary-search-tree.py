#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def f(nums):
            if not nums: return None
            n = len(nums)
            lt = f(nums[:n / 2])
            rt = f(nums[n / 2 + 1:])
            t = TreeNode(nums[n / 2])
            t.left = lt
            t.right = rt
            return t

        return f(nums)
