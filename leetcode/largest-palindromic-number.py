#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = [0] * 10
        for c in num:
            c = ord(c) - ord('0')
            cnt[c] += 1

        head = []
        for i in reversed(range(10)):
            if cnt[i] >= 2:
                head.extend([i] * (cnt[i] // 2))
        tail = head[::-1]
        mid = None
        for i in reversed(range(10)):
            if cnt[i] % 2 == 1:
                mid = i
                break

        while tail and tail[-1] == 0:
            tail.pop()
        ans = []
        ans.extend(tail[::-1])
        if mid is not None:
            ans.append(mid)
        ans.extend(tail)

        ans = ''.join([chr(ord('0') + x) for x in ans])
        if not ans: ans = '0'
        return ans


true, false, null = True, False, None
cases = [
    ("00000", '0'),
    ('00011', '10001'),
    ('444947137', '7449447'),
    ('00009', '9'),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestPalindromic, cases)

if __name__ == '__main__':
    pass
