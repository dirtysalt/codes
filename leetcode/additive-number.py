#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        if n < 3:
            return False

        def parse_int(s):
            v = int(s)
            # print(s, v)
            return v

        sz0 = 1 if num[0] == '0' else n - 2
        for i in range(1, sz0 + 1):
            a = parse_int(num[:i])

            sz1 = 1 if num[i] == '0' else n - 1 - i
            for j in range(1, sz1 + 1):
                b = parse_int(num[i: i + j])

                res = 0
                k = i + j
                ok = False
                since = k
                t0, t1 = a, b

                while k < n:
                    res = res * 10 + ord(num[k]) - ord('0')
                    if res == (t0 + t1):
                        if k == (n - 1):
                            ok = True
                            break
                        t0, t1, res = t1, res, 0
                        since = k + 1
                    elif res > (t0 + t1):
                        break
                    else:
                        if num[since] == '0':
                            break
                    k += 1

                if ok:
                    return True

        return False


cases = [
    # ("112358", True),
    # ("199100199", True),
    # ("1023", False),
    # ('0', False),
    # ('000', True),
    # ('1203', False),
    # ("111122335588143", True),
    ("101020305080130210", True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isAdditiveNumber, cases)
