#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:

        def test(arr, k):
            border = []
            for l, c, r in arr:
                if c > 1 and (r - l) > 3 * k:
                    return False
                border.append((l - k, l + k))
                border.append((r - k, r + k))
            border.sort()

            # choose X
            x = border[0][1]
            # choose Y
            y = border[0][0]
            for l, r in border:
                if x < l: y = max(y, l)

            # print(border, k, x, y)

            def ok(l, c, r):
                if abs(l - x) <= k and abs(r - x) <= k: return True
                if abs(l - y) <= k and abs(r - y) <= k: return True
                if c > 1:
                    if (y - x) > k: return False
                    if abs(l - x) <= k and abs(r - y) <= k: return True
                return False

            # right now (Y-X) maybe > k
            # but we can check if we can cover only with X
            for l, c, r in arr:
                if not ok(l, c, r): return False
            return True

        s, e = 0, max(nums)
        # arr -> list[(left, how many -1, right)]
        # left, right could be -1
        arr, l, cnt = [], -1, 0
        for i in range(len(nums)):
            if nums[i] == -1:
                cnt += 1
                continue

            if cnt != 0:
                arr.append((l, cnt, nums[i]))
                cnt = 0
            l = nums[i]

            if i > 0 and nums[i - 1] != -1:
                s = max(s, abs(nums[i - 1] - nums[i]))
            if (i + 1) < len(nums) and nums[i + 1] != -1:
                s = max(s, abs(nums[i + 1] - nums[i]))

        if cnt != 0:
            arr.append((l, cnt, -1))

        if not arr: return s
        if len(arr) == 1 and (arr[0], arr[-1]) == (-1, -1): return 0

        for i in range(len(arr)):
            l, cnt, r = arr[i]
            l = l if l != -1 else r
            r = r if r != -1 else l
            if l > r:
                l, r = r, l
            arr[i] = (l, cnt, r)

        # print(arr)

        while s <= e:
            m = (s + e) // 2
            ok = test(arr, m)
            # print(ok)
            if ok:
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, -1, 10, 8], 4),
    ([-1, -1, -1], 0),
    ([-1, 10, -1, 8], 1),
    ([14, -1, -1, 46], 11),
    ([-1, 80, -1, -1, 17], 21),
]

aatest_helper.run_test_cases(Solution().minDifference, cases)

if __name__ == '__main__':
    pass
