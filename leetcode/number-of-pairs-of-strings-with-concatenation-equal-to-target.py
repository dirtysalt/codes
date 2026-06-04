#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from collections import Counter
        cnt = Counter(nums)

        ans = 0
        for i in range(len(target) - 1):
            a = target[:i + 1]
            b = target[i + 1:]
            if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                continue
            c = cnt[a]
            d = cnt[b]

            if a == b:
                c -= 1

            ans += c * d

        return ans


if __name__ == '__main__':
    pass
