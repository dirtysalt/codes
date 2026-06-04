#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = [1 << 31] * len(nums)
        st[0] = 0
        for i in range(0, len(nums)):
            v = nums[i]
            # range = [i + 1, i + v]
            for j in range(min(len(nums) - 1, i + v), i, -1):
                if (st[i] + 1) < st[j]:
                    st[j] = st[i] + 1
                else:
                    # print('prune')
                    break
        return st[len(nums) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
    print(s.jump([1, 2, 3]))
    print(s.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]))
