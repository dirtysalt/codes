#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode import aatest_helper


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        right = [-1] * 26
        for i in reversed(range(n)):
            x = ord(S[i]) - ord('a')
            if right[x] == -1:
                right[x] = i

        ans = []
        i = 0
        while i < n:
            x = ord(S[i]) - ord('a')
            end = right[x]
            j = i + 1
            while j <= end:
                x = ord(S[j]) - ord('a')
                end = max(end, right[x])
                j += 1
            ans.append((end - i + 1))
            i = end + 1
        return ans


sol = Solution()
cases = [
    ("ababcbacadefegdehijhklij", [9, 7, 8]),
    ("abcde", [1, 1, 1, 1, 1])
]

aatest_helper.run_test_cases(sol.partitionLabels, cases)
