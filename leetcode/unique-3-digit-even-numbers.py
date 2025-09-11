#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = set()
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if i == k or j == k: continue
                    if digits[k] % 2 != 0: continue
                    value = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(value)
        # print(ans)
        return len(ans)


if __name__ == '__main__':
    pass
