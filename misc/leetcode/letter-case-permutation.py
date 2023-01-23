#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [S]
        for i in range(len(S)):
            to = None
            if S[i].upper() != S[i]:
                to = S[i].upper()
            if S[i].lower() != S[i]:
                to = S[i].lower()

            if to:
                updates = []
                for x in ans:
                    updates.append(x[:i] + to + x[i + 1:])
                ans.extend(updates)
        return ans
