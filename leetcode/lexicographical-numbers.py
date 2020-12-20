#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#
#         def run(pfx):
#             if pfx > n:
#                 return
#
#             yield pfx
#             for i in range(10):
#                 pfx2 = pfx * 10 + i
#                 yield from run(pfx2)
#
#         ans = []
#
#         for i in range(1, 10):
#             for x in run(i):
#                 ans.append(x)
#
#         return ans

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        st = []

        for i in reversed(range(1, 10)):
            st.append(i)

        ans = []
        while st:
            pfx = st.pop()
            if pfx <= n:
                ans.append(pfx)
                for i in reversed(range(10)):
                    pfx2 = pfx * 10 + i
                    st.append(pfx2)

        return ans


cases = [
    (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
    (1, [1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().lexicalOrder, cases)
