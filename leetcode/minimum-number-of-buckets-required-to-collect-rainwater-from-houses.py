#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        buck = [0] * n

        for i in range(n):
            if street[i] == '.': continue
            # check buck[i-1]
            if i > 0 and street[i - 1] == '.' and buck[i - 1]:
                continue

            # check buck[i+1]
            if (i + 1) < n and street[i + 1] == '.' and buck[i + 1]:
                continue

            # place buck[i+1]
            if (i + 1) < n and street[i + 1] == '.':
                if buck[i + 1] == 0:
                    buck[i + 1] = 1
                    continue

            # place buck[i-1]
            if i > 0 and street[i - 1] == '.':
                if buck[i - 1] == 0:
                    buck[i - 1] = 1
                    continue

            return -1

        return sum(buck)


if __name__ == '__main__':
    pass
