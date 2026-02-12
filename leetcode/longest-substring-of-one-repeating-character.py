#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        from sortedcontainers import SortedList
        A = SortedList()
        B = SortedList()
        sz, last = 1, 0
        ss = list((ord(x) - ord('a')) for x in s)
        for i in range(1, len(ss)):
            if ss[i] == ss[last]:
                sz += 1
            else:
                A.add((last, last + sz - 1, ss[last]))
                B.add(sz)
                last = i
                sz = 1
        A.add((last, last + sz - 1, ss[last]))
        B.add(sz)

        # very very error-prone. quite hard to write correct code.
        def update(p, c):
            # locate which range `p` is in.
            index = A.bisect((p,))
            if index >= len(A):
                index -= 1
            x, y, code = A[index]
            if x > p:
                index -= 1
                x, y, code = A[index]
            size = (y - x + 1)
            assert code == ss[p]
            assert x <= p <= y

            # split that range to two segments.
            del A[index]
            B.remove(size)
            t0 = x, p - 1, ss[p]
            t1 = p + 1, y, ss[p]
            insert(t0)
            insert(t1)

            # generate new segment.
            t = p, p, c
            insert(t)

        def insert(t):
            x, y, code = t
            size = (y - x + 1)
            if size == 0:
                return

            index = A.bisect((x,))
            index -= 1

            # try to merge with neighbours.
            del_vec = []
            # previous segment.
            if 0 <= index < len(A) and A[index][-1] == code:
                z0, z1, _ = A[index]
                # z0, z1, x, y
                if (z1 + 1) == x:
                    x = z0
                    del_vec.append(A[index])

            # next segment.
            if 0 <= (index + 1) < len(A) and A[index + 1][-1] == code:
                z0, z1, _ = A[index + 1]
                # x, y, z0, z1
                if (y + 1) == z0:
                    y = z1
                    del_vec.append(A[index + 1])

            if del_vec:
                for t in del_vec:
                    z0, z1, _t = t
                    size = (z1 - z0 + 1)
                    A.remove(t)
                    B.remove(size)

            A.add((x, y, code))
            size = (y - x + 1)
            B.add(size)

        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            c = ord(c) - ord('a')
            if c != ss[i]:
                update(i, c)
                ss[i] = c
            # print(A, B)
            sz = B[-1]
            ans.append(sz)
        return ans


true, false, null = True, False, None
cases = [
    ("babacc", "bcb", [1, 3, 3], [3, 3, 4]),
    ("abyzz", "aa", [2, 1], [2, 3]),
    ("geuqjmt", "bgemoegklm", [3, 4, 2, 6, 5, 6, 5, 4, 3, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]),
    ("seeu", "qjcqvsnhq", [3, 1, 0, 2, 1, 3, 3, 1, 0], [2, 1, 1, 2, 2, 1, 1, 1, 1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestRepeating, cases)

if __name__ == '__main__':
    pass
