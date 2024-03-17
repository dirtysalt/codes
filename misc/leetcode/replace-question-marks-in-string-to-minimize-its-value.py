#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(list(s))

        ans = []
        sel = []
        for c in s:
            if c == '?':
                mv, mc = 1 << 30, None
                for idx in range(26):
                    c2 = chr(ord('a') + idx)
                    if cnt[c2] < mv:
                        mv = cnt[c2]
                        mc = c2
                cnt[mc] += 1
                sel.append(mc)
        sel.sort(reverse=True)
        for c in s:
            if c == '?':
                ans.append(sel.pop())
            else:
                ans.append(c)
        # print(ans)
        return ''.join(ans)


true, false, null = True, False, None
import aatest_helper

cases = [
    ("???", "abc"),
    ("a?a?", "abac"),
    ("abcdefghijklmnopqrstuvwxy??", "abcdefghijklmnopqrstuvwxyaz")
]

aatest_helper.run_test_cases(Solution().minimizeStringValue, cases)

if __name__ == '__main__':
    pass
