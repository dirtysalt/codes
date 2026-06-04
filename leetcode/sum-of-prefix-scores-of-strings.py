#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        from collections import Counter
        cnt = Counter()
        for w in words:
            for sz in range(1, len(w) + 1):
                s = w[:sz]
                cnt[s] += 1

        ans = []
        for w in words:
            r = 0
            for sz in range(1, len(w) + 1):
                s = w[:sz]
                r += cnt[s]
            ans.append(r)
        return ans


true, false, null = True, False, None
cases = [
    (["abc", "ab", "bc", "b"], [5, 4, 3, 2]),
    (["abcd"], [4]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumPrefixScores, cases)

if __name__ == '__main__':
    pass
