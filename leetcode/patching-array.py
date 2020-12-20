#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.sort()
        k, size, value = 0, len(nums), 1

        # 确保第一个元素是1
        res = []
        if k < size and nums[k] == 1:
            k += 1
        else:
            res.append(1)

        # 不断检测当前范围和下一个值是否重叠
        # 如果不重叠的话，那么就需要插入值(value+1)，然后更新范围value=2*value+1
        # 如果重叠的话，那么不需要插入值，但是更新范围value=value+k
        while value < n:
            if k < size:
                v = nums[k]
                if v > (value + 1):
                    res.append(value + 1)
                    value = value * 2 + 1
                else:
                    value += v
                    k += 1
            else:
                res.append(value + 1)
                value = value * 2 + 1
        print(res)
        return len(res)


def test():
    cases = [
        ([], 1, 1),
        ([1, 3], 6, 1),
        ([1, 5, 10], 20, 2)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (nums, n, exp) = c
        res = sol.minPatches(nums, n)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
