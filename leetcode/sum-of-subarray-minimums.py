#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def sumSubarrayMins(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#
#         n = len(A)
#         ans = 0
#         MOD = 10 ** 9 + 7
#
#         for i in range(n):
#             j = i - 1
#             while j >= 0 and A[j] > A[i]:
#                 j -= 1
#             j += 1
#
#             k = i + 1
#             while k < n and A[k] >= A[i]:
#                 k += 1
#             k -= 1
#
#             # A[j..i] and A[i..k] uses A[i]
#             x = i - j + 1
#             y = k - i + 1
#             val = (x * y * A[i]) % MOD
#             ans = (ans + val % MOD) % MOD
#
#         return ans

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        st = []
        # (v, i, j), v = A[i]
        # j means least index which A[j] < A[i]

        MOD = 10 ** 9 + 7
        n = len(A)
        ans = 0
        for i in range(n):
            j = i
            while st and A[i] < st[-1][0]:
                x = st[-1]
                ans += x[0] * (i - x[1]) * (x[1] - x[2] + 1)
                ans = ans % MOD
                j = x[2]
                st.pop()
            st.append((A[i], i, j))

        while st:
            x = st[-1]
            ans += x[0] * (n - x[1]) * (x[1] - x[2] + 1)
            ans = ans % MOD
            st.pop()
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumSubarrayMins([3, 1, 2, 4]))
    print(sol.sumSubarrayMins([85, 93, 93, 90]))
