#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumTime(self, s: str) -> int:
        s = '1' + s + '1'
        ps = []
        tmp = []
        for i in range(len(s)):
            if s[i] == '1':
                ps.append(i)

        # suppose position of '1' are stored in ps
        # we remove consecutive head '1' from ps[i]
        # and remove consecutive tail '1' from ps[j]
        # the cost will be (ps[i] + 1) + (len(s) - ps[j]) + (j-i-1)*2
        # len(s) - 1 + (ps[i] - 2 * i) - (ps[j] - 2 * j) st. i < j
        # that's to say we have to compute min(ps[i] - 2i) and max(ps[j] - 2j)
        for i in range(len(ps)):
            tmp.append(ps[i] - 2 * i)
        right = tmp.copy()
        for i in reversed(range(1, len(right))):
            right[i - 1] = max(right[i - 1], right[i])

        ans = 1 << 30
        for i in range(len(tmp) - 1):
            res = len(s) - 1 + tmp[i] - right[i + 1]
            ans = min(ans, res)

        # because we add head and tail '1'
        ans -= 2
        return ans


true, false, null = True, False, None
cases = [
    ("1100101", 5),
    ("0010", 2),
    ("010110", 5),
    ("00000110100111110001110111000000000", 26),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumTime, cases)

if __name__ == '__main__':
    pass
