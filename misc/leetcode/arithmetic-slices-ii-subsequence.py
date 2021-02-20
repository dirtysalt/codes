#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
#

# only works for non duplicated elements.
# class Solution:
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         if n == 0: return 0
#
#         vis = [[0] * n for _ in range(n)]
#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if vis[i][j]:
#                     continue
#
#                 res = []
#                 res.append(i)
#                 res.append(j)
#                 gap = A[j] - A[i]
#                 for k in range(j + 1, n):
#                     if (A[k] - A[res[-1]]) == gap:
#                         res.append(k)
#
#                 count = len(res)
#                 ans += (count - 2) * (count - 1) // 2
#
#                 # print(res)
#                 for k in range(1, len(res)):
#                     vis[res[k - 1]][res[k]] = 1
#         return ans


# class Solution:
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         if n == 0: return 0
#         # (end, step) as key, count as value
#         st = defaultdict(int)
#         ans = 0
#         for x in A:
#             updates = defaultdict(int)
#             updates[(x, None, 1)] += 1
#             for (end, step, seq), count in st.items():
#                 if step is None:
#                     updates[(x, x - end, 2)] += count
#                 elif (x - end) == step:
#                     updates[(x, step, 3)] += count
#                     ans += count
#             for k, v in updates.items():
#                 st[k] += v
#         print(st)
#         return ans

# 这个算法和上面算法类似，但是更加简单：
# 不考虑seq==2的情况，而是直接在最后面减去C(n,2)

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        if n == 0: return 0
        dp = defaultdict(int)
        for i in range(0, n):
            for j in range(0, i):
                step = A[i] - A[j]
                dp[(i, step)] += 1
                if (j, step) in dp:
                    dp[(i, step)] += dp[(j, step)]
        ans = sum(dp.values()) - n * (n - 1) // 2
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
    print(sol.numberOfArithmeticSlices([0, 1, 2, 2, 2]))
    print(sol.numberOfArithmeticSlices([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(sol.numberOfArithmeticSlices(
        [5664, 2072, -2238, -7485, 9369, 1385, 4499, 6758, 1460, -5140, 288, -9585, 6452, -3565, 6917, 112, 3393, 1702,
         -4500, -323, -9973, 8249, 3805, -6989, -9753, -11256, 8340, -4999, -9541, -8505, 6104, 2438, 8193, -9720,
         -9678, 7155, 9191, 6897, 5030, -5757, -7799, -11021, 9187, 3122, 6587, 8721, 4385, 7510, 10157, 8886, 10275,
         11052, 10118, -7729, 7832, -1852, -6163, 7460, 7101, -4745, 3720, 4804, -66, -10257, 4106, -7813, 1730, -5576,
         4975, -10223, -2359, -7798, -515, -1673, -10094, 3282, 3190, -9630, 10576, -6806, 7145, 2184, -9624, 7291,
         -2565, -2732, -6485, 1491, -490, 6347, -6090, -5937, 6870, 1842, -5339, -4552, -2924, 8881, -8683, -11046,
         -1869, -6799, 7987, 9638, -7579, -4480, 10113, -8618, -10382, -4126, -9151, -3284, 5160, 5901, 1387, 6892, 904,
         -7253, 1065, 2809, -10824, 5777, -9972, 5721, 7692, -4863, -7085, 9566, -9299, -10204, -6134, 10862, -7064,
         3442, 8423, -5570, -5685, 1465, -1115, 3502, 4901, -3758, 120, -6541, -438, -10538, -10035, -9669, 5952, 6006,
         6575, 9832, -865, -8339, -10020, 6846, 2411, 8482, -4713, 3536, -2031, 7918, -1431, 10654, -516, -3175, -5889,
         -1651, 6399, -9821, 7726, 1507, -736, -9361, -3894, 11196, -10696, -545, -6429, -4373, -7221, 1003, -790,
         -10344, 9956, -6282, 5562, 9868, -4840, 10945, 10155, 5779, 11166, -10262, 2714, -2591, -5561, -7403, 321,
         9106]))
