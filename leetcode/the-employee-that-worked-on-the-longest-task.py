#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        p = 0
        maxt = 0
        ans = -1
        for id, lt in logs:
            t = lt - p
            p = lt
            if t >= maxt:
                if t > maxt or (t == maxt and id < ans):
                    ans = id
                maxt = t
        return ans


if __name__ == '__main__':
    pass
