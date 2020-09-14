#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class MajorityChecker:
#     def __init__(self, arr: List[int]):
#         import numpy as np
#         self.arr = np.array(arr)
#
#     def query(self, left: int, right: int, threshold: int) -> int:
#         import numpy as np
#         res = np.bincount(self.arr[left:right + 1])
#         # print(list(res), list(self.arr[left:right + 1]))
#         v = np.argmax(res)
#         if res[v] >= threshold:
#             return v
#         return -1
#

# class MajorityChecker:
#     def __init__(self, arr: List[int]):
#         from collections import defaultdict
#         pos = defaultdict(list)
#         for i, v in enumerate(arr):
#             pos[v].append(i)
#         self.pos = pos
#         self.sample_times = 20
#         self.arr = arr
#
#     def get_freq(self, v, left, right):
#         ps = self.pos[v]
#
#         def bs(x, p):
#             s, e = 0, len(x) - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if x[m] < p:
#                     s = m + 1
#                 else:
#                     e = m - 1
#             return s
#
#         # 找到第一个>=left的pos
#         a = bs(ps, left)
#         # 找到第一个<=right的pos.
#         # 等于找到第一个>=(right+1)的pos, 然后-1?
#         b = bs(ps, right + 1) - 1
#         return b - a + 1
#
#     def query(self, left: int, right: int, threshold: int) -> int:
#         import random
#         # 没有采样到的概率是 (1/2) ^ sample_times
#         for _ in range(self.sample_times):
#             i = random.randint(left, right)
#             v = self.arr[i]
#             freq = self.get_freq(v, left, right)
#             if freq >= threshold:
#                 return v
#         return -1

class SegTree:
    def __init__(self):
        self.val = self.freq = 0
        self.left = self.right = None
        self.start = self.end = 0


def bm_vote(a: SegTree, b: SegTree, c: SegTree):
    if a.val == b.val:
        c.val = a.val
        c.freq = a.freq + b.freq
        return

    if b.freq < a.freq:
        a, b = b, a

    c.val = b.val
    c.freq = b.freq - a.freq
    return


def build_seg_tree(arr, s, e):
    if s > e:
        return None
    if s == e:
        t = SegTree()
        t.val = arr[s]
        t.freq = 1
        t.start = s
        t.end = e
        return t

    m = (s + e) // 2
    left = build_seg_tree(arr, s, m)
    right = build_seg_tree(arr, m + 1, e)
    t = SegTree()
    t.start = s
    t.end = e
    t.left = left
    t.right = right
    bm_vote(left, right, t)
    return t


def query_seg_tree(t, s, e):
    if s <= t.start and t.end <= e:
        return t
    m = (t.start + t.end) // 2
    if (m + 1) > e:
        # 只搜索左边
        x = query_seg_tree(t.left, s, e)
    elif m < s:
        x = query_seg_tree(t.right, s, e)
    else:
        a = query_seg_tree(t.left, s, m)
        b = query_seg_tree(t.right, m + 1, e)
        x = SegTree()
        bm_vote(a, b, x)
    return x


class MajorityChecker:
    def __init__(self, arr: List[int]):
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
        self.pos = pos
        self.arr = arr
        self.st = build_seg_tree(arr, 0, len(arr) - 1)

    def get_freq(self, v, left, right):
        ps = self.pos[v]

        def bs(x, p):
            s, e = 0, len(x) - 1
            while s <= e:
                m = (s + e) // 2
                if x[m] < p:
                    s = m + 1
                else:
                    e = m - 1
            return s

        # 找到第一个>=left的pos
        a = bs(ps, left)
        # 找到第一个<=right的pos.
        # 等于找到第一个>=(right+1)的pos, 然后-1?
        b = bs(ps, right + 1) - 1
        return b - a + 1

    def query(self, left: int, right: int, threshold: int) -> int:
        t = query_seg_tree(self.st, left, right)
        freq = self.get_freq(t.val, left, right)
        if freq >= threshold:
            return t.val
        return -1


import aatest_helper

null = None
cases = [
    (["MajorityChecker", "query", "query", "query"], [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]],
     [null, 1, -1, 2]),

]
aatest_helper.run_simulation_cases(MajorityChecker, cases)
