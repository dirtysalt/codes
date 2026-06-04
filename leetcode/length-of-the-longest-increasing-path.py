#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:

        def search(arr):
            # x in arr
            # order by x[0]
            dp = [arr[0][1]]
            i = 1
            while i < len(arr):
                # 相同的x需要批量更新，不然会出现序列错误
                j = i
                values = []
                while j < len(arr):
                    if arr[j][0] == arr[i][0]:
                        values.append(arr[j][1])
                        j += 1
                    else:
                        break
                i = j

                # 本质上这里还是使用二分搜索找到插入点的位置
                def search(y):
                    s, e = 0, len(dp) - 1
                    while s <= e:
                        m = (s + e) // 2
                        if dp[m] >= y:
                            e = m - 1
                        else:
                            s = m + 1
                    return s

                pos = [search(y) for y in values]
                for p, y in zip(pos, values):
                    if p == len(dp):
                        dp.append(y)
                    elif p != 0:
                        dp[p] = min(dp[p], y)
            return len(dp)

        A, B = [], []
        for i in range(len(coordinates)):
            x, y = coordinates[i]
            if i == k:
                A.append((x, y))
                B.append((x, y))
                continue

            if x < coordinates[k][0]:
                A.append((x, y))
            elif x > coordinates[k][0]:
                B.append((x, y))

        A.sort(reverse=True)
        A = [(x[0], -x[1]) for x in A]
        B.sort()
        a, b = search(A), search(B)
        return a + b - 1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[5, 0], [9, 3], [9, 8]], 0, 2),
    ([[3, 6], [7, 3], [6, 9]], 1, 1),
    ([[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], 1, 3),
    ([[2, 1], [7, 0], [5, 6]], 2, 2),
    ([[4, 7], [6, 8], [0, 3], [6, 0]], 0, 3),
    ([[9, 5], [1, 4], [1, 7], [9, 8], [6, 4], [6, 7]], 3, 3),
    ([[0, 6], [0, 2], [2, 9], [8, 9], [1, 0]], 2, 2)
]

aatest_helper.run_test_cases(Solution().maxPathLength, cases)

if __name__ == '__main__':
    pass
