#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isThree(self, n: int) -> bool:

        cnt = 0
        for m in range(1, n + 1):
            if n % m == 0:
                cnt += 1
                if cnt > 3:
                    return False
        return cnt == 3


if __name__ == '__main__':
    pass
