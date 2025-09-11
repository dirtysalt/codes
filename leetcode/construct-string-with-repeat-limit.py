#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = [0] * 26
        for c in s:
            c2 = ord(c) - ord('a')
            count[c2] += 1

        n = len(s)
        lastIndex = -1
        ans = []
        while True:
            index = -1
            for i in reversed(range(26)):
                if count[i] != 0 and i != lastIndex:
                    index = i
                    break
            if index == -1:
                break
            used = min(count[index], repeatLimit)
            if lastIndex > index and count[lastIndex]:
                used = 1
            ans.extend([index] * used)
            count[index] -= used
            lastIndex = index

        ans = ''.join((chr(x + ord('a')) for x in ans))
        return ans


true, false, null = True, False, None
cases = [
    ("cczazcc", 3, "zzcccac"),
    ("aababab", 2, "bbabaa")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().repeatLimitedString, cases)

if __name__ == '__main__':
    pass
