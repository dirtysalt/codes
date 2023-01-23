#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right[-1] = 1
        for i in reversed(range(n - 1)):
            if security[i + 1] >= security[i]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1

        ans = []
        for i in range(n):
            if left[i] > time and right[i] > time:
                ans.append(i)
        return ans


if __name__ == '__main__':
    pass
