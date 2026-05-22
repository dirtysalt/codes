#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


#
# class Solution:
#     def threeSumMulti(self, A: List[int], target: int) -> int:
#         A.sort()
#         n = len(A)
#
#         P = 10 ** 9 + 7
#         ans = 0
#         for i in range(0, n - 2):
#             for j in range(i + 1, n - 1):
#                 lookup = target - A[i] - A[j]
#                 arr = A[j + 1:]
#                 if lookup < arr[0] or lookup > arr[-1]:
#                     continue
#                 import bisect
#                 x = bisect.bisect_left(arr, lookup)
#                 y = bisect.bisect_right(arr, lookup)
#                 # print(arr, lookup, x, y)
#                 ans += (y - x)
#                 ans = ans % P
#         return ans

# class Solution:
#     def threeSumMulti(self, A: List[int], target: int) -> int:
#         A.sort()
#         n = len(A)
#
#         P = 10 ** 9 + 7
#         ans = 0
#         for i in range(0, n - 2):
#             j, k = i + 1, n - 1
#             while j < k:
#                 v = A[i] + A[j] + A[k]
#                 if v == target:
#                     if A[j] == A[k]:
#                         # C(n, 2)
#                         sz = (k - j + 1)
#                         ans += sz * (sz - 1) // 2
#                         ans = ans % P
#                         break
#
#                     else:
#                         j2 = j + 1
#                         while A[j2] == A[j2 - 1]: j2 += 1
#                         k2 = k - 1
#                         while A[k2] == A[k2 + 1]: k2 -= 1
#                         szj = j2 - j
#                         szk = k - k2
#                         ans += (szj * szk)
#                         ans = ans % P
#
#                         j = j2
#                         k = k2
#
#                 elif v > target:
#                     k -= 1
#                 else:
#                     j += 1
#
#         return ans

# class Solution:
#     def threeSumMulti(self, A: List[int], target: int) -> int:
#         A.sort()
#         n = len(A)
#
#         right_next = [-1] * n
#         left_next = [-1] * n
#
#         left_next[0] = 0
#         for i in range(1, n):
#             if A[i] == A[i - 1]:
#                 left_next[i] = left_next[i - 1]
#             else:
#                 left_next[i] = i
#         right_next[-1] = n - 1
#         for i in reversed(range(0, n - 1)):
#             if A[i] == A[i + 1]:
#                 right_next[i] = right_next[i + 1]
#             else:
#                 right_next[i] = i
#
#         P = 10 ** 9 + 7
#         ans = 0
#         for i in range(0, n - 2):
#             j, k = i + 1, n - 1
#             while j < k:
#                 v = A[i] + A[j] + A[k]
#                 if v == target:
#                     if A[j] == A[k]:
#                         # C(n, 2)
#                         sz = (k - j + 1)
#                         ans += sz * (sz - 1) // 2
#                         ans = ans % P
#                         break
#
#                     else:
#                         j2 = right_next[j] + 1
#                         k2 = left_next[k] - 1
#                         szj = j2 - j
#                         szk = k - k2
#                         ans += (szj * szk)
#                         ans = ans % P
#
#                         j = j2
#                         k = k2
#
#                 elif v > target:
#                     k -= 1
#                 else:
#                     j += 1
#
#         return ans

# class Solution:
#     def threeSumMulti(self, A: List[int], target: int) -> int:
#         P = 10 ** 9 + 7
#         from collections import Counter
#         counter = Counter(A)
#         keys = list(counter.keys())
#         keys.sort()
#         n = len(keys)
#
#         ans = 0
#
#         if target % 3 == 0:
#             num = target // 3
#             v = counter[num]
#             if v >= 3:
#                 ans += (v * (v - 1) * (v - 2)) // 6
#                 ans = ans % P
#
#         def C2(n):
#             v = n * (n - 1) // 2
#             return v % P
#
#         for i in range(n):
#             for j in range(i, n):
#                 ki, kj = keys[i], keys[j]
#                 v = target - ki - kj
#                 if v < kj or (i == j and v == kj):  # 重复选择，之前将i, j, k属于一个集合排除
#                     break
#
#                 res = 0
#                 if i == j:  # i, j 属于同一集合
#                     # C(counter[ki], 2) * counter[v]
#                     res = C2(counter[ki]) * counter[v]
#                 elif v == kj:  # j, k 属于同一集合
#                     # counter[ki] * C(counter[kj], 2)
#                     res = counter[ki] * C2(counter[kj])
#                 else:  # 分属不同集合
#                     res = counter[ki] * counter[kj] * counter[v]
#
#                 # print(ki, kj, v, res)
#                 ans += res % P
#                 ans = ans % P
#
#         return ans

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        P = 10 ** 9 + 7

        from collections import Counter
        counter = Counter(A)
        keys = list(counter.keys())
        keys.sort()
        n = len(keys)

        def C2(n):
            v = n * (n - 1) // 2
            return v % P

        def C3(n):
            v = n * (n - 1) * (n - 2) // 6
            return v % P

        ans = 0

        for i in range(n):
            j, k = i, n - 1
            while j <= k:
                v = keys[i] + keys[j] + keys[k]
                if v == target:
                    res = 0
                    if i == j == k:
                        res = C3(counter[keys[i]])
                    elif i == j:
                        res = C2(counter[keys[j]]) * counter[keys[k]]
                    elif j == k:
                        res = counter[keys[i]] * C2(counter[keys[j]])
                    else:
                        res = counter[keys[i]] * counter[keys[j]] * counter[keys[k]]
                    ans += res % P
                    ans = ans % P
                    j += 1
                    k -= 1
                elif v > target:
                    k -= 1
                else:
                    j += 1

        return ans


import aatest_helper

cases = [
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
    ([1, 1, 2, 2, 2, 2], 5, 12),
    ([0, 0, 0], 0, 1),
    ([0] * 1000, 0, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().threeSumMulti, cases)
