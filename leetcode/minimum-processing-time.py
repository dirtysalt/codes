#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0
        for i in range(len(processorTime)):
            p = processorTime[i]
            t = tasks[4 * i]
            ans = max(ans, p + t)
        return ans


if __name__ == '__main__':
    pass
