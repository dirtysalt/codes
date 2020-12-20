#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        if n == 0:
            return []

        threshold = n // 3

        def pivot(nums, s, e):
            i = s
            for j in range(s, e):
                if nums[j] < nums[e]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[e] = nums[e], nums[i]
            return i

        ans = []

        def search(nums, s, e):
            if (e - s + 1) <= threshold:
                return

            # nums[s .. p0 - 1] < nums[p0]
            p0 = pivot(nums, s, e)
            search(nums, s, p0 - 1)

            # nums[p0 .. e] >= nums[p0]
            if (e - p0 + 1) > threshold:
                value = nums[p0]
                j = p0 + 1
                for i in range(p0 + 1, e + 1):
                    if nums[i] == value:
                        nums[i], nums[j] = nums[j], nums[i]
                        j += 1
                if (j - p0) > threshold:
                    ans.append(value)

                search(nums, j, e)

        search(nums, 0, n - 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
