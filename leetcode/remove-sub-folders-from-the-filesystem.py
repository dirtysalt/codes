#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        def is_prefix(a, b):
            if len(a) < len(b):
                return a == b[:len(a)] and b[len(a)] == '/'
            return False

        pfx = '-'
        ans = []
        for s in folder:
            if is_prefix(pfx, s):
                continue
            else:
                pfx = s
                ans.append(pfx)

        return ans


cases = [
    (["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"], ["/a", "/c/d", "/c/f"])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().removeSubfolders, cases)
