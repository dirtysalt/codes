#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s):
            res = 0
            for m in range(1, 27):
                if k * m > len(word):
                    break
                cnt = [0] * 26
                cat = m
                for i in range(len(s)):
                    j = i - (k * m)
                    if j >= 0:
                        cnt[s[j]] -= 1
                        now = cnt[s[j]]
                        if (now + 1) in (0, k):
                            cat -= 1
                        if now in (0, k):
                            cat += 1

                    cnt[s[i]] += 1
                    if True:
                        now = cnt[s[i]]
                        if (now - 1) in (0, k):
                            cat -= 1
                        if now in (0, k):
                            cat += 1

                    if (i + 1) >= k * m and cat == m:
                        res += 1
            return res

        ss = [ord(x) - ord('a') for x in word]
        ans = 0
        j = 0
        for i in range(len(ss)):
            if i > 0 and abs(ss[i] - ss[i - 1]) > 2:
                ans += f(ss[j:i])
                j = i
        ans += f(ss[j:])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("igigee", 2, 3),
    ("aaabbbccc", 3, 6),
    ("aab", 1, 4),
    ("ba", 1, 3),
]

aatest_helper.run_test_cases(Solution().countCompleteSubstrings, cases)

if __name__ == '__main__':
    pass
