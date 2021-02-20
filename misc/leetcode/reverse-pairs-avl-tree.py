#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

def height(r):
    return r.height if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(height(root.left), height(root.right)) + 1

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    root.total -= left.total
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

    right.left = root
    right.height = max(height(right.left), height(right.right)) + 1
    right.total += root.total
    return right


def balance(root):
    lh = height(root.left)
    rh = height(root.right)

    if (lh - rh) >= 2:
        llh = height(root.left.left)
        lrh = height(root.left.right)
        if lrh > llh:
            root.left = right_rotate(root.left)
        root = left_rotate(root)

    elif (rh - lh) >= 2:
        rlh = height(root.right.left)
        rrh = height(root.right.right)
        if rlh > rrh:
            root.right = left_rotate(root.right)
        root = right_rotate(root)

    else:
        root.height = max(lh, rh) + 1

    return root


class Tree:
    def __init__(self, v):
        self.v = v
        self.own = 1 # 自己数量
        self.total = 1 # <=v的总数
        self.left = self.right = None
        self.height = 1

def insert_tree(t: Tree, v):
    if t is None:
        return Tree(v)
    if v == t.v:
        t.own += 1
        t.total += 1
        return t

    if v < t.v:
        t.left = insert_tree(t.left, v)
        t.total += 1
    else:
        t.right = insert_tree(t.right, v)
    t = balance(t)
    return t

def query_tree(t: Tree, max_exp):
    if t is None:
        return 0

    if t.v > max_exp:
        # 只需要搜索左边
        return query_tree(t.left, max_exp)

    # t.v <= max_exp
    res = t.total
    if t.v < max_exp:
        res += query_tree(t.right, max_exp)
    return res

# note(yan): 这个方向是正确的，但是对于有序的序列就没有办法了，除非手写旋转树。还是找找python有什么自带的实现吧
# N年前写的AVL模板还是可以用上的. 这个模板特别好用是你只要固定好字段left, right, height, 当然还需要做简单调整
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        t = None
        ans = 0
        for i in reversed(range(len(nums))):
            v = nums[i]
            max_exp = (v - 1) // 2
            ans += query_tree(t, max_exp)
            t = insert_tree(t, v)
        return ans

    def native(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        n = len(nums)
        ans = 0
        for i in reversed(range(n-1)):
            v = nums[i]
            for j in range(i+1, n):
                if v > 2 * nums[j]:
                    ans += 1
        return ans


cases = [
    ([1, 3, 2, 3, 1], 2),
    ([2, 4, 3, 5, 1], 3),
    ([-5, -5], 1),
    ([12, 2, 1, 17, 19, 10, 5, 23, 7, 20, 10, 17, 22, 15, 9, 18, 12, 12, 16, 16, 17, 8, 11, 19, 2, 21, 5, 19, 22, 9, 17,
      24, 8, 8, 16, 5, 2, 25, 1, 0, 3, 24, 25, 0, 11, 7, 19, 0, 5, 16, 17, 4, 19, 20, 20, 0, 14, 4, 16, 15, 11, 15, 20,
      11, 17, 13, 3, 18, 12, 6, 10, 25, 12, 6, 18, 6, 19, 19, 18, 13, 21, 9, 17, 1, 1, 2, 10, 15, 24, 24, 22, 7, 10, 23,
      15, 9, 1, 23, 22, 15, 3, 16, 23, 25, 8, 18, 0, 5, 1, 12, 9, 0, 25, 0, 13, 11, 22, 5, 3, 13, 10, 17, 14, 24, 23, 1,
      8, 1, 21, 18, 2, 16, 21, 21, 5, 3, 19, 8, 23, 6, 6, 3, 2, 4, 13, 2, 4, 14, 9, 17, 23, 18, 4, 23, 5, 13, 25, 10, 9,
      14, 3, 9, 11, 5, 14, 18, 0, 10, 13, 5, 19, 17, 24, 25, 4, 8, 16, 14, 3, 24, 18, 2, 17, 22, 4, 11, 18, 9, 9, 7, 10,
      4, 24, 0, 7, 0, 6, 15, 18, 13, 14, 20, 22, 17, 22, 15, 17, 9, 10, 17, 13, 0, 22, 22, 23, 2, 21, 18, 6, 10, 10, 15,
      14, 4, 4, 18, 21, 15, 0, 18, 14, 0, 2, 24, 6, 10, 1, 8, 25, 20, 13, 20, 13, 20, 5, 21, 21, 9, 19, 8, 9, 9, 5, 17,
      18, 18, 20, 5, 17, 18, 3, 7, 21, 6, 0, 8, 3, 3, 1, 11, 0, 21, 6, 15, 11, 10, 13, 6, 7, 21, 7, 1, 1, 14, 15, 20, 2,
      8, 21, 25, 19, 12, 18, 16, 0, 4, 10, 19, 14, 23, 6, 17, 2, 15, 19, 4, 13, 8, 14, 4, 15, 21, 4, 23, 20, 3, 18, 0,
      12, 14, 14, 19, 0, 21, 18, 21, 17, 13, 9, 20, 17, 25, 17, 21, 16, 22, 4, 1, 13, 20, 15, 9, 7, 18, 18, 7, 22, 8,
      18, 1, 13, 0, 24, 8, 12, 16, 1, 3, 6, 23, 16, 24, 5, 0, 1, 25, 3, 16, 9, 4, 24, 1, 11, 24, 9, 16, 11, 0, 2, 20,
      16, 0, 1, 6, 19, 22, 12, 3, 23, 21, 4, 20, 1, 0, 18, 24, 10, 0, 12, 21, 17, 23, 0, 13, 1, 25, 9, 19, 0, 13, 21,
      23, 6, 24, 25, 16, 9, 8, 16, 2, 22, 23, 3, 7, 16, 25, 11, 18, 19, 4, 11, 1, 25, 22, 9, 11, 14, 9, 3, 16, 8, 5, 11,
      12, 15, 15, 19, 15, 15, 7, 17, 24, 18, 9, 8, 20, 23, 18, 17, 7, 8, 19, 23, 9, 13, 4, 17, 23, 21, 19, 11, 22, 22,
      9, 3, 19, 23, 11, 2, 23, 8, 8, 21, 15, 1, 25, 7, 6, 14, 6, 7, 11, 3, 2, 11, 14, 10, 24, 3, 8, 10, 1, 18, 4, 6, 16,
      12, 18, 12, 6, 5, 25, 24, 25, 7, 12, 17, 19, 15, 8, 23, 7, 6, 11, 6, 16, 14, 15, 13, 18, 5, 9, 21, 24, 8, 17, 25,
      21, 22, 19, 24, 9, 9, 25, 21, 6, 25, 24, 3, 15, 20, 19, 13, 7, 13, 3, 0, 11, 2, 3, 23, 4, 14, 13, 7, 14, 3, 2, 18,
      6, 1, 24, 19, 11, 6, 22, 9, 20, 3, 15, 23, 14, 18, 11, 11, 0, 2, 14, 21, 1, 12, 8, 8, 22, 10, 25, 20, 15, 22, 15,
      21, 4, 19, 23, 5, 20, 4, 10, 17, 9, 7, 8, 11, 7, 10, 2, 18, 5, 24, 4, 16, 22, 13, 0, 11, 6, 19, 8, 21, 23, 24, 14,
      19, 6, 3, 1, 17, 25, 22, 9, 14, 12, 15, 2, 24, 23, 17, 3, 3, 3, 6, 11, 20, 11, 0, 12, 17, 0, 3, 12, 24, 5, 13, 11,
      19, 5, 2, 5, 12, 20, 19, 23, 2, 14, 23, 19, 4, 6, 15, 12, 2, 24, 17, 18, 9, 18, 4, 12, 20, 17, 19, 21, 16, 15, 13,
      0, 17, 10, 23, 22, 10, 8, 20, 6, 4, 13, 11, 0, 3, 1, 5, 19, 17, 23, 17, 10, 10, 7, 4, 1, 20, 21, 23, 21, 21, 25,
      2, 1, 8, 22, 4, 10, 16, 9, 15, 12, 12, 7, 3, 10, 14, 11, 9, 0, 7, 1, 1, 18, 23, 16, 6, 4, 20, 17, 18, 20, 17, 22,
      8, 19, 6, 8, 14, 23, 14, 14, 15, 3, 24, 19, 16, 18, 14, 3, 6, 10, 8, 22, 12, 6, 8, 5, 3, 20, 10, 15, 19, 17, 8,
      10, 7, 22, 0, 5, 19, 18, 16, 22, 24, 6, 18, 19, 19, 21, 1, 22, 14, 0, 24, 1, 20, 21, 7, 2, 11, 13, 10, 9, 7, 13,
      15, 22, 2, 17, 4, 1, 4, 22, 22, 7, 18, 3, 12, 12, 7, 6, 20, 15, 25, 8, 13, 7, 5, 1, 25, 12, 1, 25, 16, 3, 23, 25,
      9, 22, 4, 11, 16, 21, 20, 15, 17, 16, 13, 14, 20, 5, 23, 9, 0, 6, 3, 21, 2, 7, 2, 22, 7, 5, 8, 17, 14, 17, 8, 18,
      21, 22, 14, 8, 15, 2, 10, 24, 0, 10, 23, 11, 16, 22, 5, 5, 19, 20, 14, 2, 19, 3, 25, 5, 10, 14, 22, 3, 5, 10, 20,
      22, 16, 17, 22, 15, 23, 10, 0, 21, 17, 20, 3, 15, 0, 13, 17, 2, 10, 20, 8, 24, 5, 6, 19, 9, 4, 25, 11, 19, 10, 3,
      24, 0, 10, 10, 9, 21, 16, 25, 6, 20, 11, 7, 17, 20, 10, 9, 22, 19, 21, 7, 0, 4, 11, 1, 9, 18, 18, 3, 1, 25, 5, 1,
      20, 13, 2, 7, 19, 10, 13, 25, 3, 23, 13, 5, 10, 15, 11, 15, 22, 9, 10, 8, 18, 0], 124430),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().reversePairs, cases)
