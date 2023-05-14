#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def age(x):
            return int(x[-4:-2])

        ans = 0
        for d in details:
            if age(d) > 60:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
