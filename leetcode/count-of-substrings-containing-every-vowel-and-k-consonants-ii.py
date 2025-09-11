#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        from collections import Counter

        n = len(word)
        next = [n] * n
        p = n
        for i in reversed(range(n)):
            next[i] = p
            if word[i] not in 'aeoiu':
                p = i

        cnt = Counter()
        oth = 0

        def put(c, d):
            nonlocal cnt, oth
            if c in 'aeoiu':
                cnt[c] += d
                if cnt[c] == 0:
                    del cnt[c]
            else:
                oth += d

        ans = 0
        j = 0
        for i in range(len(word)):
            c = word[i]
            put(c, 1)

            while oth > k:
                c = word[j]
                j += 1
                put(c, -1)

            while len(cnt) == 5 and oth == k:
                ans += next[i] - i
                c = word[j]
                j += 1
                put(c, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("aeioqq", 1, 0),
    ("aeiou", 0, 1),
    ("ieaouqqieaouqq", 1, 3),
    ("iqeaouqi", 2, 3),
]

aatest_helper.run_test_cases(Solution().countOfSubstrings, cases)

if __name__ == '__main__':
    pass
