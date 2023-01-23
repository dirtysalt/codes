#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ss = [ord(x) - ord('a') for x in s]
        rs = [[-1, -1] for _ in range(26)]
        n = len(ss)
        for i in range(n):
            c = ss[i]
            if rs[c][0] == -1:
                rs[c][0] = i
            rs[c][1] = i

        ext = rs.copy()
        for c in range(26):
            p0, p1 = rs[c]
            if p0 == -1:
                continue

            changed = True
            while changed:
                changed = False
                cs = set(ss[p0:p1 + 1])
                p2, p3 = p0, p1
                for i in range(26):
                    if i not in cs: continue
                    p2 = min(p2, rs[i][0])
                    p3 = max(p3, rs[i][1])
                if p2 != p0 or p3 != p1:
                    changed = True
                p0, p1 = p2, p3
            ext[c] = [p0, p1]

        ext = [(x, y) for x, y in ext if x != -1]
        ext.sort(key=lambda x: (x[1], -x[0]))
        st = []
        for x, y in ext:
            if st and st[-1][1] >= x:
                continue
            st.append((x, y))

        ans = []
        for x, y in st:
            ans.append(s[x:y + 1])
        ans.sort(key=lambda x: (len(x), x))
        return ans


import aatest_helper

cases = [
    ("adefaddaccc", ["e", "f", "ccc"]),
    ("abbaccd", ["d", "bb", "cc"]),
    ("ababa", ["ababa"]),
]

aatest_helper.run_test_cases(Solution().maxNumOfSubstrings, cases)
