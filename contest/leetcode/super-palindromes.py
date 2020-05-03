#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        cache = {}

        def gen_par(bits):
            if bits in cache:
                return cache[bits]

            if bits == 1:
                ans = list(range(10))
            elif bits == 2:
                ans = list([x * 11 for x in range(10)])
            else:
                res = gen_par(bits - 2)
                tmp = []
                base = 10 ** (bits - 1)
                for x in range(10):
                    for y in res:
                        tmp.append(x * base + y * 10 + x)
                ans = tmp
            cache[bits] = ans
            return ans

        def gen_nums(bits):
            if bits == 1:
                yield from range(1, 10)
            elif bits == 2:
                yield from (x * 11 for x in range(1, 10))
            else:
                base = 10 ** (bits - 1)
                res = gen_par(bits - 2)
                for x in range(1, 10):
                    for y in res:
                        yield x * base + y * 10 + x

        def is_par(x2):
            seq = []
            while x2:
                seq.append(x2 % 10)
                x2 = x2 // 10
            return seq == seq[::-1]

        L = int(L)
        R = int(R)
        ans = 0
        for bits in range(1, 10):
            for x in gen_nums(bits):
                x2 = x * x
                # print(x)
                if x2 > R:
                    break
                if x2 < L:
                    continue
                # print(x, x2)
                if is_par(x2):
                    # print('>>>', x, x2)
                    ans += 1
        return ans


cases = [
    ("4", "1000", 4),
    ("1", "19028", 8),
    ("1", "1" + "0" * 18, 70),
    ("92904622", "232747148", 6),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().superpalindromesInRange, cases)
