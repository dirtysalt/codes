#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 类似这种需要使用tree来辅助计数，可能都可以用归并排序来解决
# 不过使用tree的可有可能出现不平衡的情况，所以还要加上balance操作

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0: return []

        ans = [0] * len(nums)

        def merge(xs):
            if len(xs) == 1:
                return xs

            m = len(xs) // 2
            left = merge(xs[:m])
            right = merge(xs[m:])

            i = len(left) - 1
            j = len(right) - 1
            tmp = []
            while i >= 0 or j >= 0:
                if j == -1 or (i >= 0 and left[i][1] > right[j][1]):
                    ans[left[i][0]] += (j + 1)
                    tmp.append(left[i])
                    i -= 1
                else:
                    tmp.append(right[j])
                    j -= 1
            return tmp[::-1]

        merge(list(enumerate(nums)))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([5, 2, 6, 1]))
