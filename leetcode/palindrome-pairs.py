#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        from collections import defaultdict
        front_matches = defaultdict(list)
        back_matches = defaultdict(list)

        for (idx, w) in enumerate(words):
            for sz in range(0, len(w) + 1):
                # print(w[:sz], w[sz:])
                a, b = w[:sz], w[sz:]
                if sz and a == a[::-1]:
                    left = b[::-1]
                    front_matches[left].append(idx)
                if b == b[::-1]:
                    left = a[::-1]
                    back_matches[left].append(idx)

        # print(matches)

        ans = []
        for (idx, w) in enumerate(words):
            res = front_matches[w]
            ans.extend([[idx, x] for x in res if x != idx])
            res = back_matches[w]
            ans.extend(([x, idx] for x in res if x != idx))

        ans.sort()
        return ans


cases = [
    (["abcd", "dcba", "lls", "s", "sssll"], sorted([[0, 1], [1, 0], [3, 2], [2, 4]])),
    (["a", ""], sorted([[0, 1], [1, 0]])),
    (["a", "b", "c", "ab", "ac", "aa"], sorted([[3, 0], [1, 3], [4, 0], [2, 4], [5, 0], [0, 5]]))
]

import aatest_helper

aatest_helper.run_test_cases(Solution().palindromePairs, cases)
