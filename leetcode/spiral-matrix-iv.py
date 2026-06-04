#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeList(values):
    head = ListNode()
    now = head
    for x in values:
        now.next = ListNode(x)
        now = now.next
    return head.next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        vis = set()
        d = 0
        i, j = 0, -1
        while head:
            x = head.val
            head = head.next
            while True:
                i2, j2 = i, j
                if d == 0:
                    j += 1
                elif d == 1:
                    i += 1
                elif d == 2:
                    j -= 1
                elif d == 3:
                    i -= 1

                if i < 0 or i >= m or j < 0 or j >= n or (i, j) in vis:
                    i, j = i2, j2
                    d = (d + 1) % 4
                else:
                    break
            # print(i, j, x)
            ans[i][j] = x
            vis.add((i, j))
        return ans


true, false, null = True, False, None
cases = [
    (3, 5, makeList([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]), [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]),
    (1, 4, makeList([0, 1, 2]), [[0, 1, 2, -1]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().spiralMatrix, cases)

if __name__ == '__main__':
    pass
