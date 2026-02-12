#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class PrefixSumTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (n + 1)
        self.n = n
        for i in range(n):
            self.update_sum(i, arr[i])

    def get_sum(self, index):
        t = 0
        index = index + 1
        while index > 0:
            t += self.tree[index]
            index -= index & (-index)
        return t

    def update_sum(self, index, val):
        index = index + 1
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        peaks = [0] * n
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                peaks[i] = 1
        pst = PrefixSumTree(peaks)

        def update(idx):
            new = int(nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1])
            old = peaks[idx]
            pst.update_sum(idx, new - old)
            peaks[idx] = new

        ans = []
        for q in queries:
            if q[0] == 1:
                r = pst.get_sum(q[2])
                # have to remove q[2]
                if peaks[q[2]]:
                    r -= 1

                l = 0
                if q[1] > 0:
                    l = pst.get_sum(q[1] - 1)
                    # have to remove q[1]
                    if peaks[q[1]]:
                        l += 1
                #  print(l, r)
                # when q[1] == q[2]
                ans.append(max(r - l, 0))
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                if idx - 2 >= 0:
                    update(idx - 1)
                if idx - 1 >= 0 and idx + 1 < n:
                    update(idx)
                if (idx + 2) < n:
                    update(idx + 1)
                # print(nums)
        return ans

true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]], res=[0]),
    aatest_helper.OrderedDict(nums=[4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]], res=[0, 1]),
    ([2, 3, 2, 5, 2], [[1, 1, 3], [1, 1, 4]], [0, 1]),
    ([5, 4, 8, 6], [[1, 2, 2], [1, 1, 2], [2, 1, 6]], [0, 0]),
    ([8, 10, 10, 9, 10], [[2, 0, 1], [2, 2, 7], [1, 0, 2]], [1]),
]

aatest_helper.run_test_cases(Solution().countOfPeaks, cases)

if __name__ == '__main__':
    pass
