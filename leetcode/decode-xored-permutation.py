#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        # encoded[i] = perm[i] ^ perm[i+1]

        # get p0^p1, p0^p2 ... p0^p(n-1)
        # them xor all which is p1^p2^...p(n-1) as A
        # then we know 1^2^...n as B
        # then we know p0 = A ^ B


        n = len(encoded) + 1
        B = 0
        for i in range(1, n+1):
            B = B ^ i

        t = 0
        A = 0
        for x in encoded:
            t = t ^ x
            A = A ^ t

        p0 = A ^ B
        ans = [p0]
        t = 0
        for x in encoded:
            t = t ^ x
            ans.append(t ^ p0)
        return ans

cases = [
    ([3,1], [1,2,3]),
    ([6,5,4,6], [2,4,1,5,3]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().decode, cases)
