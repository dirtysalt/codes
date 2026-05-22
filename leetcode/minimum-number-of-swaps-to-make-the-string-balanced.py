#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minSwaps(self, s: str) -> int:
        # preprocess, to remove balanced pairs.
        buf = []
        for c in s:
            if c == '[':
                buf.append(1)
            elif c == ']':
                if buf and buf[-1] == 1:
                    buf.pop()
                else:
                    buf.append(0)

        left = 0
        right = 0

        ans = 0
        for c in buf:
            if c == 1:
                left += 1
            elif c == 0:
                if left > 0:
                    left -= 1
                else:
                    right += 1

            # since we already remove balanced pairs.
            # the left ones must be like  ']]][[['
            if left == right:
                ans += (left + 1) // 2
        return ans


true, false, null = True, False, None
cases = [
    ("][][", 1),
    ("]]][[[", 2),
    ("[]", 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSwaps, cases)

if __name__ == '__main__':
    pass
