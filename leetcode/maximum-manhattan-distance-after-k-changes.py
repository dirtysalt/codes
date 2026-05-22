#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dxy = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        def toward(ex, ey, k):
            ans = 0
            x, y = 0, 0
            for c in s:
                dx, dy = dxy[c]
                if (ex * dx < 0 or ey * dy < 0) and k > 0:
                    dx = -dx
                    dy = -dy
                    k -= 1
                x, y = x + dx, y + dy
                ans = max(ans, abs(x) + abs(y))
            return ans

        ans = 0
        for ex, ey in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            res = toward(ex, ey, k)
            ans = max(ans, res)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ('NWSE', 1, 3),
    ('NSWWEW', 3, 6),
    ('NSES', 1, 4),
]

aatest_helper.run_test_cases(Solution().maxDistance, cases)

if __name__ == '__main__':
    pass
