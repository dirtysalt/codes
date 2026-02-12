#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# note(yan): 这个算法是可行的，虽然时间和内存开销都比较高
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        m = len(nums2)

        maxd1 = nums1.copy()
        maxd2 = nums2.copy()
        for i in reversed(range(n - 1)):
            maxd1[i] = max(maxd1[i], maxd1[i + 1])
        for i in reversed(range(m - 1)):
            maxd2[i] = max(maxd2[i], maxd2[i + 1])

        cache = {}

        def fn(i, j, k):
            if k == 0:
                return ''

            cache_key = '{}.{}.{}'.format(i, j, k)
            if cache_key in cache:
                return cache[cache_key]

            cs = []

            # pre-compute max first digit.

            # 在可以选择的范围内最大的字符
            max_fd = -1
            # 实际上最大的字符. 如果实际上后面还有更大的字符，那么我们当前是不能连续选择max_fd
            # 因为理论上可以空出来选择后面更大的字符
            act_max_fd = -1
            for idx in range(i, n):
                if ((n - idx) + (m - j)) < k:
                    break
                max_fd = max(max_fd, nums1[idx])
            for idx in range(j, m):
                if ((n - i) + (m - idx)) < k:
                    break
                max_fd = max(max_fd, nums2[idx])

            if i != n:
                act_max_fd = max(act_max_fd, maxd1[i])
            if j != m:
                act_max_fd = max(act_max_fd, maxd2[j])
            use_longest = (max_fd == act_max_fd)

            # ensure first digit is max_fd
            # search first digit is max_fd
            idx = i
            while idx < n and ((n - idx) + (m - j)) >= k and nums1[idx] != max_fd:
                idx += 1

            # use max_id as much as possible. 当然是在允许longest的模式下
            if idx < n and nums1[idx] == max_fd:
                last = idx
                while idx < n and ((n - idx) + (m - j)) >= k and nums1[idx] == max_fd and (k >= (idx - last + 1)):
                    idx += 1
                    if not use_longest:
                        break

                sz = (idx - last)
                if sz != 0:
                    assert (k >= sz)
                    x = fn(idx, j, k - sz)
                    x = (chr(max_fd + ord('0')) * sz) + x
                    cs.append(x)

            # 对第二个序列也做同样操作
            idx = j
            while idx < m and ((n - i) + (m - idx)) >= k and nums2[idx] != max_fd:
                idx += 1
            if idx < m and nums2[idx] == max_fd:
                last = idx
                while idx < m and ((n - i) + (m - idx)) >= k and nums2[idx] == max_fd and (k >= (idx - last + 1)):
                    idx += 1
                    if not use_longest:
                        break
                sz = (idx - last)
                if sz != 0:
                    assert (k >= sz)
                    x = fn(i, idx, k - sz)
                    x = (chr(max_fd + ord('0')) * sz) + x
                    cs.append(x)

            x = max(cs)
            cache[cache_key] = x
            return x

        ans = fn(0, 0, k)
        ans = [ord(x) - ord('0') for x in ans]
        return ans


# note(yan): 下面这个算法是看示例代码的，非常简单。分解成为两个问题：
#  1. 从每个序列中选择k'个数字形成最大的序列
#  2. 然后将两个序列合并

class Solution:
    def maxNumber(self, nums1, nums2, k):

        def max_seq(xs, exp):
            cs = []
            drop = len(xs) - exp
            for x in xs:
                # 可以尽可能保证前面数字尽可能的大，但是又确保后面可以选择到数字
                while drop and cs and cs[-1] < x:
                    cs.pop()
                    drop -= 1
                cs.append(x)
            return cs[:exp]

        def merge(a, b):
            # 这个写法的确是出乎意料
            return [max(a, b).pop(0) for _ in a + b]

        ans = max([merge(max_seq(nums1, k1), max_seq(nums2, k2))
                   for k1 in range(len(nums1) + 1)
                   for k2 in range(len(nums2) + 1)
                   if (k1 + k2) == k])
        return ans


import aatest_helper

cases = [
    ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
    ([3, 4, 6, 5], [8, 3], 4, [8, 6, 5, 3]),
    ([6, 3, 1, 7, 6, 6, 1, 4, 7, 8, 4, 1, 4, 6, 1, 0, 8, 9, 6, 2, 3, 1, 5, 4, 9, 5, 4, 2, 1, 7, 7, 1, 4, 0, 6, 2, 8, 6,
      2, 4, 9, 8, 5, 5, 5, 1, 3, 5, 4, 2, 3, 8, 4, 1, 1, 1, 0, 9, 6, 7, 2, 3, 8, 9, 0, 3, 3, 4, 6, 3, 7, 7, 0, 7, 9, 7,
      2, 8, 8, 9, 8, 0, 8, 2, 1, 9, 8, 0, 8, 4],
     [6, 4, 1, 5, 0, 8, 7, 6, 3, 2, 7, 7, 4, 1, 1, 5, 3, 5, 5, 9, 2, 2, 0, 8, 0, 5, 7, 3, 9, 9, 1, 2, 2, 4, 2, 7, 4, 5,
      1, 5, 6, 4, 7, 5, 5,
      0, 0, 9, 7, 3, 4, 2, 3, 1, 6, 8, 9, 8, 3, 7, 2, 8, 5, 8, 5, 4, 4, 7, 6, 8, 1, 0, 0, 5, 7, 9, 5, 1, 6, 8, 9, 7, 8,
      6, 8, 6, 7, 5, 2, 7],
     90,
     [9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 5, 4, 3, 5, 5, 9, 2, 2, 0, 8, 0, 5, 7, 3, 9, 9, 1, 2, 2, 4, 2, 7, 4, 5,
      1, 5, 6, 4, 7, 5, 5,
      0, 0, 9, 7, 3, 4, 2, 3, 1, 6, 8, 9, 8, 3, 7, 2, 8, 5, 8, 5, 4, 4, 7, 6, 8, 1, 0, 0, 5, 7, 9, 5, 1, 6, 8, 9, 7, 8,
      6, 8, 6, 7, 5, 2, 7]
     ),
    ([6, 6, 8], [5, 0, 9], 3, [9, 6, 8]),
    ([2, 1, 2, 0, 2, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 1, 2, 0, 0, 1, 2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 1, 0,
      0, 2, 2, 1, 1, 1, 1, 2, 0, 2, 0, 2, 2, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 0,
      2, 1, 2, 0, 0, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 1, 2, 1, 0, 0, 0, 1, 0, 2, 0,
      1, 1, 1, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 1, 1, 1, 1, 0, 2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 2, 1, 1, 1,
      0, 2, 1, 0, 0, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 2, 0, 0, 1, 1, 0, 2, 2, 2, 1, 2, 2, 0, 2, 2, 2, 2, 2,
      1, 0, 0, 0, 2, 1, 0, 1, 0, 1]
     ,
     [1, 2, 1, 2, 2, 0, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 0, 0, 0, 2, 2, 0, 2, 0, 0, 1, 0, 1, 1, 1, 0, 2, 2,
      2, 0, 1, 1, 1, 0, 2, 2, 1, 2, 0, 0, 2, 0, 1, 1, 0, 1, 0, 0, 0, 2, 0, 1, 0, 1, 2, 1, 1, 0, 2, 2, 0, 2, 0, 0, 0, 1,
      0, 2, 2, 0, 2, 0, 0, 2, 1, 0, 2, 1, 2, 2, 1, 2, 0, 1, 1, 0, 2, 0, 0, 1, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 1, 1, 1,
      2, 2, 1, 1, 0, 1, 1, 2, 1, 0, 2, 0, 1, 1, 2, 0, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 2, 1, 1,
      1, 0, 2, 2, 0, 1, 2, 2, 2, 1, 2, 1, 0, 2, 2, 0, 1, 0, 2, 1, 2, 2, 1, 0, 1, 1, 0, 2, 0, 1, 1, 2, 0, 0, 0, 2, 0, 1,
      0, 1, 1, 2, 0, 1, 2, 1, 2, 0],
     400, aatest_helper.ANYTHING),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     100, aatest_helper.ANYTHING),
    ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]),
    ([6, 7, 5], [4, 8, 1], 3, [8, 7, 5]),

]
aatest_helper.run_test_cases(Solution().maxNumber, cases)
