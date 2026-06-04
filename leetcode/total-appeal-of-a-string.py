#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def appealSum(self, s: str) -> int:
        pos = [[] for _ in range(26)]
        for i in reversed(range(len(s))):
            c = ord(s[i]) - ord('a')
            pos[c].append(i)

        ans = 0
        for i in range(len(s)):
            ps = []
            for j in range(26):
                if pos[j]:
                    ps.append(pos[j][-1])
            ps.sort()
            ps.append(len(s))

            c = ord(s[i]) - ord('a')
            pos[c].pop()

            res = 0
            w = 1
            for j in range(1, len(ps)):
                d = ps[j] - ps[j - 1]
                res += w * d
                w += 1

            # print(i, res)
            ans += res

        return ans


true, false, null = True, False, None
cases = [
    ("abbca", 28),
    ("code", 20),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().appealSum, cases)

if __name__ == '__main__':
    pass
