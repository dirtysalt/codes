#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def rotate(B):
            n, m = len(B), len(B[0])
            C = [[None] * n for _ in range(m)]
            for i in range(n):
                for j in range(m):
                    C[m - 1 - j][i] = B[i][j]
            return C

        def check(B):
            # print('========')
            # for x in B:
            #     print(x)

            n, m = len(B), len(B[0])
            for i in range(n):
                ps = []
                j = 0
                while True:
                    while j < m and B[i][j] == '#':
                        j += 1
                    j2 = j
                    while j < m and B[i][j] != '#':
                        j += 1
                    if j > j2:
                        ps.append((j2, j))
                    if j == m:
                        break

                for j, j2 in ps:
                    if (j2 - j) == len(word):
                        ok = True
                        for k in range(j, j2):
                            if B[i][k] == ' ' or B[i][k] == word[k - j]:
                                pass
                            else:
                                ok = False
                                break
                        if ok:
                            return True
            return False

        B = board
        for _ in range(4):
            B = rotate(B)
            if check(B): return True

        return False


true, false, null = True, False, None
cases = [
    ([["#", " ", "#"], ["#", " ", "#"], ["#", " ", "c"]], "ca", True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().placeWordInCrossword, cases)

if __name__ == '__main__':
    pass
