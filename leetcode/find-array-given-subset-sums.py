#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()

        def split(data):
            delta = data[1] - data[0]
            from collections import Counter
            used = Counter()
            total = Counter(data)

            left, right = [], []
            for i in range(len(data)):
                x = data[i]
                if used[x]:
                    used[x] -= 1
                    continue
                left.append(x)
                exp = delta + x
                total[exp] -= 1
                used[exp] += 1
                right.append(exp)

            return left, right, delta

        def search(data, ans):
            if len(data) == 1:
                return data[0] == 0

            left, right, exp = split(data)
            if 0 in left:
                ans.append(exp)
                if search(left, ans):
                    return True
                ans.pop()

            if 0 in right:
                ans.append(-exp)
                if search(right, ans):
                    return True
                ans.pop()
            return False

        ans = []
        ok = search(sums, ans)
        return ans


import aatest_helper

true, false, null = True, False, None
cases = [
    (3, [-3, -2, -1, 0, 0, 1, 2, 3], [1, 2, -3]),
    (2, [0, 0, 0, 0], [0, 0]),
    (4, [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8], [0, -1, 4, 5]),
    (2, [-1654, -771, -883, 0], [-771, -883]),
    (3, [365, 44, -355, 399, 409, 764, 10, 0], [-355, 365, 399]),
    (5,
     [0, 1084, 380, -1571, -72, -776, -48, 332, 43, -1234, -361, -463, 795, -530, -867, -126, -1156, -150, -487, -337,
      747, -24, 458, -819, -945, -752, -415, -439, 669, -1282, 265, 289], aatest_helper.ANYTHING),
]

aatest_helper.run_test_cases(Solution().recoverArray, cases)

if __name__ == '__main__':
    pass
