#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def test(key, k, flip):
            j = 0
            n = len(key)

            ans = 0
            for i in range(n):
                if key[i] == flip:
                    if k == 0:
                        while key[j] != flip:
                            j += 1
                        j += 1
                        k += 1
                    k -= 1
                ans = max(ans, i - j + 1)

            # print(ans)
            return ans

        a = test(answerKey, k, 'F')
        b = test(answerKey, k, 'T')
        return max(a, b)


true, false, null = True, False, None
cases = [
    ("TTFTTFTT", 1, 5),
    ("TTFF", 2, 4),
    ("TFFT", 1, 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxConsecutiveAnswers, cases)

if __name__ == '__main__':
    pass
