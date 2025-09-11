#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # check L and R is equal
        def count(s):
            a, b = 0, 0
            for c in s:
                if c == 'L':
                    a += 1
                elif c == 'R':
                    b += 1
            return a, b

        a, b = count(start)
        c, d = count((target))
        if (a, b) != (c, d):
            return False

        n = len(start)
        # move L first.
        last = 0
        for i in range(n):
            if start[i] == target[i]: continue
            if target[i] == 'L':
                if start[i] == '_':
                    # search following 'L'
                    last = max(last, i + 1)
                    while last < n and start[last] == '_':
                        last += 1
                    if last < n and start[last] == 'L':
                        last += 1
                        pass
                    else:
                        return False
                else:
                    return False

        # move R later.
        last = n - 1
        for i in reversed(range(n)):
            if start[i] == target[i]: continue
            if target[i] == 'R':
                if start[i] == '_':
                    # search preceding 'R'
                    last = min(last, i - 1)
                    while last >= 0 and start[last] == '_':
                        last -= 1
                    if last >= 0 and start[last] == 'R':
                        last -= 1
                        pass
                    else:
                        return False
                else:
                    return False
        return True


true, false, null = True, False, None
cases = [
    ("_L__R__R_", "L______RR", true),
    ('R_L_', '__LR', false),
    ('_R', 'R_', false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canChange, cases)

if __name__ == '__main__':
    pass
