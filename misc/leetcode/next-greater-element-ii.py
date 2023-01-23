#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        if n == 0: return []

        xs = []
        ans = [-1] * n
        max_value = max(nums)

        def check(v, xs):
            s, e = 0, len(xs) - 1
            while s <= e:
                m = (s + e) // 2
                if nums[xs[m]] >= v:
                    s = m + 1
                else:
                    e = m - 1

            for k in range(s, len(xs)):
                ans[xs[k]] = v
            xs = xs[:s]
            return xs

        for i in range(n):
            if ans[i] != -1:
                continue
            xs = check(nums[i], xs)
            if nums[i] != max_value:
                xs.append(i)

        for i in range(n):
            xs = check(nums[i], xs)
            if not xs:
                break

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([2]))
    print(sol.nextGreaterElements([1, 2, 1]))
    print(sol.nextGreaterElements([1, 2, 3, 4, 5]))
    print(sol.nextGreaterElements([1, 3, 2, 4, 6, 5]))
    print(sol.nextGreaterElements([1, 2, 3, 2, 1]))
    print(sol.nextGreaterElements([1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3]))
