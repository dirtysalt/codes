#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            j -= 1
            sz = j - i + 1
            szs = str(sz)

            if len(szs) <= (j - i):
                chars[k] = chars[i]
                k += 1
                for c in szs:
                    chars[k] = c
                    k += 1
            else:
                for k2 in range(i, j + 1):
                    chars[k] = chars[k2]
                    k += 1

            i = j + 1
        return k


cases = [
    (["a", "a", "b", "b", "c", "c", "c"], 6),
    (['a', 'b'], 2),
    (["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().compress, cases)
