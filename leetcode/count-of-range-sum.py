#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import bisect


# 这里bisect.insort还是O(n)的时间复杂度，但是可以通过tree来解决。
# 如此说来，如果可能需要使用tree作为辅助计数的时候，最好考虑一下是否可以用merge sort来完成。

# class Solution:
#     def countRangeSum(self, nums, lower, upper):
#         """
#         :type nums: List[int]
#         :type lower: int
#         :type upper: int
#         :rtype: int
#         """
#
#         history = [0]
#         ans = 0
#         acc = 0
#         for x in nums:
#             acc += x
#
#             l, r = acc - upper, acc - lower
#             # history[li..] >= l
#             li = bisect.bisect_left(history, l)
#             # history[..ri] <= r
#             ri = bisect.bisect_right(history, r)
#             ans += (ri - li)
#
#             print(history, acc, l, r, ri - li)
#
#             bisect.insort(history, acc)
#         return ans

class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(0, n):
            sums[i + 1] = sums[i] + nums[i]

        def merge(xs, s, e):
            if s == e:
                return 0

            # merge sort这个部分的切分非常重要
            m = (s + e) // 2 + 1
            ans = merge(xs, s, m - 1)
            ans += merge(xs, m, e)

            p, q = m, m
            for i in range(s, m):
                while p <= e and xs[p] - xs[i] < lower:
                    p += 1
                while q <= e and xs[q] - xs[i] <= upper:
                    q += 1
                ans += (q - p)

            tmp = []
            i, j = s, m
            while i < m or j <= e:
                if j > e or (i < m and xs[i] < xs[j]):
                    tmp.append(xs[i])
                    i += 1
                else:
                    tmp.append(xs[j])
                    j += 1
            xs[s:e + 1] = tmp
            return ans

        # print(sums)
        ans = merge(sums, 0, len(sums) - 1)
        # print(sums)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countRangeSum([-2, 5, -1], -2, 2))
    print(sol.countRangeSum([-1, 1], 0, 0))
