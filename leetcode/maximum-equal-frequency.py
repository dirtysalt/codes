#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        freq = Counter()

        def is_ok(freq):
            if len(freq) > 2:
                return False

            xs = list(freq.items())
            if len(xs) == 1:
                # 出现f次的元素有c个
                # 如果减掉其中1个的话
                # 那么有f次c-1个，和f-1次1个
                # (f, c-1) + (f-1, 1)
                (f, c) = xs[0]
                if c == 1 or f == 1:
                    return True
                return False

            if xs[0][0] < xs[1][0]:
                xs[0], xs[1] = xs[1], xs[0]
            (f1, c1) = xs[0]
            (f2, c2) = xs[1]
            # print(f1, c1, f2, c2)
            # 如果减去f1
            # (f1, c1-1), (f1-1,1), (f2, c2)
            if c1 == 1 and (f1 - 1) == f2:
                return True
            # 如果减去f2
            # (f1, c1), (f2-1, 1), (f2, c2-1)
            if f2 == 1 and c2 == 1:
                return True
            return False

        ans = 0
        size = 0

        for x in nums:
            cnt[x] += 1
            v = cnt[x] - 1
            freq[v + 1] += 1
            if freq[v] > 0:
                freq[v] -= 1
                if freq[v] == 0:
                    del freq[v]

            size += 1
            # print(freq)
            if is_ok(freq):
                ans = max(ans, size)
        return ans
