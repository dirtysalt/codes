#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countTime(self, time: str) -> int:
        time = time.replace(":", '')

        def walk(i, ss):
            if i == 4:
                h = ss[0] * 10 + ss[1]
                m = ss[2] * 10 + ss[3]
                x = h * 60 + m
                if x < 1440 and h < 24 and m < 60:
                    return 1
                return 0

            ans = 0
            if time[i] == '?':
                for j in range(10):
                    ss.append(j)
                    ans += walk(i + 1, ss)
                    ss.pop()
            else:
                ss.append(ord(time[i]) - ord('0'))
                ans += walk(i + 1, ss)
                ss.pop()
            return ans

        return walk(0, [])


true, false, null = True, False, None
cases = [
    ("?5:00", 2),
    ("0?:0?", 100),
    ("??:??", 1440),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countTime, cases)

if __name__ == '__main__':
    pass
