#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        from sortedcontainers import SortedList
        opts = [SortedList(), SortedList()]
        for i in range(n):
            opts[i % 2].add(i)
        for x in banned:
            opts[x % 2].remove(x)

        from collections import deque
        dq = deque()
        ans = [-1] * n
        dq.append(p)
        ans[p] = 0
        opts[p % 2].remove(p)

        def search(x):
            y = max(x + 1 - k, k - x - 1, 0)
            if (x + y + 1) % 2 != k % 2:
                y += 1
            opt = opts[y % 2]
            idx = opt.bisect_left(y)
            while idx < len(opt):
                y = opt[idx]
                a, b = x, y
                if a > b:
                    a, b = b, a
                m = (k - (b - a + 1)) // 2
                if m >= 0 and (a - m) >= 0 and (b + m) < n:
                    yield a if a != x else b
                else:
                    break
                idx += 1

        while dq:
            x = dq.popleft()
            values = []
            for y in search(x):
                values.append(y)

            print(x, values)
            for v in values:
                opts[v % 2].remove(v)

            for y in values:
                ans[y] = ans[x] + 1
                dq.append(y)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, 0, [1, 2], 4, [0, -1, -1, 1]),
    (4, 2, [], 4, [-1, 1, 0, -1]),
    (5, 0, [2, 4], 3, [0, -1, -1, -1, -1]),
    (4, 2, [0, 1, 3], 1, [-1, -1, 0, -1]),
    (5, 0, [], 2, [0, 1, 2, 3, 4]),
    (3, 2, [], 3, [1, -1, 0]),
]

cases += aatest_helper.read_cases_from_file('tmp.in', 5)

aatest_helper.run_test_cases(Solution().minReverseOperations, cases)

if __name__ == '__main__':
    pass
