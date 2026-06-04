#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:

        ans = list(num)
        fix = -1
        for i in range(len(ans)):
            d = ord(ans[i]) - ord('0')
            d2 = change[d]
            if d2 > d:
                fix = i
                break

        while fix < len(ans):
            d = ord(ans[fix]) - ord('0')
            d2 = change[d]
            if d2 >= d:
                ans[fix] = chr(d2 + ord('0'))
                fix += 1
            else:
                break

        return ''.join(ans)


if __name__ == '__main__':
    pass
