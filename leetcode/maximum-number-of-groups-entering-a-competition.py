#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ans = 1
        n = len(grades)
        while True:
            if ans * (ans + 1) // 2 > n:
                break
            ans += 1
        return ans - 1


if __name__ == '__main__':
    pass
