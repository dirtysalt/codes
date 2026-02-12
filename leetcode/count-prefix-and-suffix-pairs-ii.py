#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        from collections import Counter

        BASE = 13131
        MOD = 151217133020331712151

        def get_hash(w):
            h = 0
            for c in w:
                h = h * BASE + ord(c) - ord('a')
                h = h % MOD
            return h

        hashes = [(len(w), get_hash(w)) for w in words]
        cnt = Counter(hashes)

        ans = 0
        for i in reversed(range(len(words))):
            h = hashes[i]
            w = words[i]
            cnt[h] -= 1

            a, b, shift = 0, 0, 1
            for i in range(len(w)):
                a = a * BASE + ord(w[i]) - ord('a')
                b = (ord(w[len(w) - 1 - i]) - ord('a')) * shift + b
                shift = shift * BASE
                a, b, shift = a % MOD, b % MOD, shift % MOD
                if a == b:
                    ans += cnt[(i + 1, a)]
        return ans


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        from collections import Counter
        cnt = Counter()
        ans = 0
        for w in words:
            for sz in range(1, len(w) + 1):
                if sz in cnt and w[:sz] == w[-sz:]:
                    ans += cnt[(sz, w[:sz])]
            cnt[(len(w), w)] += 1
            cnt[len(w)] += 1

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (["aab", "a", "cba", "a"], 1),
    (["b", "a", "b", "a", "b"], 4),
    (["a", "aba", "ababa", "aa"], 4),
    (["pa", "papa", "ma", "mama"], 2),
    (["abab", "ab"], 0),
]

cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().countPrefixSuffixPairs, cases)

if __name__ == '__main__':
    pass
