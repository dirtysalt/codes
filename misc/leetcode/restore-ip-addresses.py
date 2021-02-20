#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []
        n = len(s)

        def dfs(i, k):
            if i == n:
                if k == 0:
                    ans.append('.'.join(path))
                return

            if k == 0: return
            v = 0
            for j in range(i, n):
                v = v * 10 + ord(s[j]) - ord('0')
                if v > 255:
                    break
                if s[i] == '0' and (j - i + 1) >= 2:
                    break
                path.append(s[i:j + 1])
                dfs(j + 1, k - 1)
                path.pop()
            return

        dfs(0, 4)
        return ans
