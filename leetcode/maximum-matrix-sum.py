#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        import heapq
        hp = []
        ans = 0
        for i in range(n):
            for j in range(n):
                hp.append(matrix[i][j])
                ans += matrix[i][j]
        heapq.heapify(hp)
        while True:
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            if (x + y) < 0:
                ans -= 2 * (x + y)
                heapq.heappush(hp, -x)
                heapq.heappush(hp, -y)
            else:
                break
        return ans


true, false, null = True, False, None
cases = [
    ([[-1, 0, -1], [-2, 1, 3], [3, 2, 2]], 15),
    ([[1, -1], [-1, 1]], 4),
    ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16),

]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxMatrixSum, cases)

if __name__ == '__main__':
    pass
