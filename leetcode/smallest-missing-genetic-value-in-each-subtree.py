#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        child = [[] for _ in range(n)]
        inorder = [0] * n

        for i in range(n):
            p = parents[i]
            if p != -1:
                child[p].append(i)
                inorder[p] += 1
        rs = [[] for _ in range(n)]
        from collections import deque
        dq = deque()
        for i in range(n):
            if inorder[i] == 0:
                rs[i] = [(nums[i], nums[i] + 1)]
                dq.append(i)

        def merge(x):
            hp = []
            for c in child[x]:
                hp.extend(rs[c])
            hp.append((nums[x], nums[x] + 1))
            import heapq
            heapq.heapify(hp)

            ans = []
            a, b = heapq.heappop(hp)
            while hp:
                c, d = heapq.heappop(hp)
                if b == c:
                    b = d
                else:
                    ans.append((a, b))
                    a, b = c, d
            ans.append((a, b))
            return ans

        # top-sort.
        while dq:
            x = dq.popleft()
            if child[x]:
                rs[x] = merge(x)

            p = parents[x]
            if p != -1:
                inorder[p] -= 1
                if inorder[p] == 0:
                    dq.append(p)

        ans = []
        for i in range(n):
            a, b = rs[i][0]
            # print(i, a, b)
            if a == 1:
                ans.append(b)
            else:
                ans.append(1)
        return ans


true, false, null = True, False, None
cases = [
    ([-1, 0, 0, 2], [1, 2, 3, 4], [5, 1, 1, 1]),
    ([-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3], [7, 1, 1, 4, 2, 1]),
    ([-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8], [1, 1, 1, 1, 1, 1, 1]),
    ([-1, 5, 3, 0, 8, 9, 0, 5, 0, 6], [7, 9, 6, 4, 8, 1, 5, 10, 3, 2], [11, 1, 1, 1, 1, 2, 3, 1, 1, 3]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestMissingValueSubtree, cases)

if __name__ == '__main__':
    pass
