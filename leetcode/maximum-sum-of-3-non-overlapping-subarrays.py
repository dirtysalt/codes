#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        acc = []
        value = sum(nums[:k])
        acc.append(value)
        for i in range(k, len(nums)):
            value -= nums[i - k]
            value += nums[i]
            acc.append(value)

        n = len(acc)

        # must TLE. O(n^3)
        # cache = {}
        # INT_MIN = -(1 << 31)
        #
        # def query(cnt, idx):
        #     if cnt == 0:
        #         return 0, []
        #     if idx >= len(acc):
        #         return INT_MIN, []
        #     key = '{}.{}'.format(cnt, idx)
        #     if key in cache:
        #         return cache[key]
        #
        #     res = INT_MIN
        #     path = []
        #     for s in range(idx, len(acc)):
        #         sub, items = query(cnt - 1, s + k)
        #         if sub != INT_MIN and (sub + acc[s]) > res:
        #             res = (sub + acc[s])
        #             path = [s] + items
        #     cache[key] = (res, path)
        #     return res, path
        #
        # res, items = query(3, 0)
        # return items

        # DP solution works. but super long. O(n)
        # dp = [0] * n
        # src = [-1] * n
        # dp[n - 1] = acc[n - 1]
        # src[n - 1] = n - 1
        # for i in range(n - 2, -1, -1):
        #     if dp[i + 1] > acc[i]:
        #         dp[i] = dp[i + 1]
        #         src[i] = src[i + 1]
        #     else:
        #         dp[i] = acc[i]
        #         src[i] = i
        #
        # dp2 = [0] * (n - k)
        # src2 = [-1] * (n - k)
        # dp2[n - k - 1] = acc[n - k - 1] + dp[n - 1]
        # src2[n - k - 1] = n - k - 1
        # for i in range(n - k - 2, -1, -1):
        #     if dp2[i + 1] > (dp[i + k] + acc[i]):
        #         dp2[i] = dp2[i + 1]
        #         src2[i] = src2[i + 1]
        #     else:
        #         dp2[i] = acc[i] + dp[i + k]
        #         src2[i] = i
        #
        # k2 = 2 * k
        # dp3 = [0] * (n - k2)
        # src3 = [-1] * (n - k2)
        # dp3[n - k2 - 1] = acc[n - k2 - 1] + dp2[n - k - 1]
        # src3[n - k2 - 1] = n - k2 - 1
        # for i in range(n - k2 - 2, -1, -1):
        #     if dp3[i + 1] > (dp2[i + k] + acc[i]):
        #         dp3[i] = dp3[i + 1]
        #         src3[i] = src3[i + 1]
        #     else:
        #         dp3[i] = acc[i] + dp2[i + k]
        #         src3[i] = i
        #
        # res = []
        # v = src3[0]
        # res.append(v)
        # v = src2[v + k]
        # res.append(v)
        # v = src[v + k]
        # res.append(v)
        # return res

        left = [0] * n
        lidx = [-1] * n
        left[0] = acc[0]
        lidx[0] = 0
        for i in range(1, n):
            if acc[i] > left[i - 1]:
                lidx[i] = i
                left[i] = acc[i]
            else:
                lidx[i] = lidx[i - 1]
                left[i] = left[i - 1]

        right = [0] * n
        ridx = [-1] * n
        right[n - 1] = acc[n - 1]
        ridx[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if acc[i] > right[i + 1]:
                ridx[i] = i
                right[i] = acc[i]
            else:
                ridx[i] = ridx[i + 1]
                right[i] = right[i + 1]

        res = 0
        items = []
        for i in range(k, n - k):
            value = left[i - k] + acc[i] + right[i + k]
            if value > res:
                res = value
                items = [lidx[i - k], i, ridx[i + k]]
        return items


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
