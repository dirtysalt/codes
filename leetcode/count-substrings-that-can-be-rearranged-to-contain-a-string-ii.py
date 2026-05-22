#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        from collections import Counter
        cnt2 = Counter(word2)
        cnt = Counter()
        miss = set(cnt2.keys())

        i = 0
        ans = 0
        while i < len(word1):
            c = word1[i]
            i += 1
            cnt[c] += 1
            if cnt[c] == cnt2[c]:
                miss.remove(c)
                if not miss:
                    ans += len(word1) - i + 1
                    break

        for j, c in enumerate(word1):
            cnt[c] -= 1
            if cnt[c] + 1 == cnt2[c]:
                miss.add(c)
                while i < len(word1):
                    c2 = word1[i]
                    i += 1
                    cnt[c2] += 1
                    if c2 == c:
                        miss.remove(c)
                        break
            if not miss:
                ans += len(word1) - i + 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("bcca", "abc", 1),
    ("abcabc", "abc", 10),
    ("abcabc", "aaabc", 0),
    ("dcbdcdccb", "cdd", 18),

]

aatest_helper.run_test_cases(Solution().validSubstringCount, cases)

if __name__ == '__main__':
    pass
