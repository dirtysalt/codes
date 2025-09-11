#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        from collections import Counter
        tc = Counter()
        print(len(s), len(t))
        for sz in range(1, len(t) + 1):
            for i in range(len(t) - sz + 1):
                ts = t[i: i + sz]
                tc[ts] += 1

        ans = 0
        for i in range(len(s)):
            for c in range(26):
                c2 = chr(ord('a') + c)
                if s[i] == c2: continue

                for j in range(i + 1):
                    for k in range(i, len(s)):
                        ss = s[j:i] + c2 + s[i + 1:k + 1]
                        v = tc[ss]
                        if v == 0:  # 更长的串肯定也没有办法匹配上
                            break
                        ans += v

        return ans


cases = [
    ("aba", "baba", 6),
    ("ab", "bb", 3),
    ("a", "a", 0),
    ("abe", "bbc", 10),
    ("qapwoavjdxsfiwohmgpszkdarjhrtbwrztmvthqvhfwhgrunsxpqcdbmebbvgebbmguytxccafqybhpmcwtombcfsa",
     "frqbamnjicyngosecgecdijivxodluabvfoaqigyqktfcszshyvmxfjldqfrirdebqgmwpbootsugvbiulkirkxrey", 8406)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSubstrings, cases)
