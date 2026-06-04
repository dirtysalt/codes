#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        child = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            child[p].append(i)

        # print(n, len(s))

        def search(i):
            if len(child[i]) == 0:
                return 1, 1, 1

            r, r2, r3 = 1, 1, 1
            d = []
            for j in child[i]:
                a, b, c = search(j)
                if s[i] != s[j]:
                    r = max(r, a + 1)
                    d.append(a)
                r3 = max(r3, c)

            r2 = r
            if len(d) >= 2:
                d.sort()
                r2 = d[-1] + d[-2] + 1

            r3 = max(r3, r2)
            return r, r2, r3

        _, _, r3 = search(0)
        return r3


true, false, null = True, False, None
cases = [
    ([-1, 0, 0, 1, 1, 2], "abacbe", 3),
    ([-1, 0, 0, 0], "aabc", 3),
    ([-1, 0], "mm", 1),
    ([-1, 0, 1], "aab", 2),
    ([-1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18, 155, 65, 13, 163,
      125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23, 101, 76, 57, 89, 4, 161, 16, 139,
      29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107, 91, 52, 42, 93, 85, 125, 89, 132, 13, 141, 21,
      152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129, 0, 19, 148, 65, 125, 41, 38, 104, 115, 130, 164, 138, 108, 65,
      31, 13, 60, 29, 116, 26, 58, 118, 10, 138, 14, 28, 91, 60, 47, 2, 149, 99, 28, 154, 71, 96, 60, 106, 79, 129, 83,
      42, 102, 34, 41, 55, 31, 154, 26, 34, 127, 42, 133, 113, 125, 113, 13, 54, 132, 13, 56, 13, 42, 102, 135, 130, 75,
      25, 80, 159, 39, 29, 41, 89, 85, 19],
     "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal",
     17)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestPath, cases)

if __name__ == '__main__':
    pass
