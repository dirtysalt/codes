#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0

        for i in range(len(bank)):
            c = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    c += 1
            if c != 0:
                ans += prev * c
                prev = c

        return ans


if __name__ == '__main__':
    pass
