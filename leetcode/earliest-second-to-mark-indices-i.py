#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        changeIndices = [x - 1 for x in changeIndices]

        def test(count, t):
            n = len(count)

            # 按照最后选择顺序进行标记
            pos = [-1] * n
            for i in reversed(range(t)):
                j = changeIndices[i]
                if pos[j] == -1:
                    pos[j] = i

            # 确保所有节点都标记上
            if any((x == -1 for x in pos)):
                return False

            change = [-1] * t
            for i in range(n):
                change[pos[i]] = i

            # 按照visit顺序对节点进行标记.
            visit = list(range(n))
            visit.sort(key=lambda x: pos[x])

            count = nums.copy()
            j = 0
            for i in range(n):
                x = visit[i]
                while count[x] != 0 and j < t:
                    if change[j] == -1:
                        change[j] = x
                        count[x] -= 1
                    elif count[change[j]] != 0:
                        return False
                    j += 1
                if count[x] != 0:
                    return False

            return True

        # 二分测试看是否满足
        s, e = len(nums), len(changeIndices)
        while s <= e:
            m = (s + e) // 2
            if test(nums, m):
                e = m - 1
            else:
                s = m + 1
        ans = s
        if ans > len(changeIndices):
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 2, 0], changeIndices=[2, 2, 2, 2, 3, 2, 2, 1], res=8),
    aatest_helper.OrderedDict(nums=[1, 3], changeIndices=[1, 1, 1, 2, 1, 1, 1], res=6),
    aatest_helper.OrderedDict(nums=[0, 1], changeIndices=[2, 2, 2], res=-1),
]

aatest_helper.run_test_cases(Solution().earliestSecondToMarkIndices, cases)

if __name__ == '__main__':
    pass
