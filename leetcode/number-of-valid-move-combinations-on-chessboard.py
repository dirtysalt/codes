#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

N = 8


def gen_one_moves(r, c, step, dr, dc):
    out = []
    for i in range(step):
        r, c = r + dr, c + dc
        out.append((r, c))
    return out


def gen_moves(r, c, p):
    moves = []
    if p == 'rook':
        dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    elif p == 'bishop':
        dxy = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    else:
        dxy = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))

    moves.append([(r, c)])

    for step in range(1, N + 1):
        for dr, dc in dxy:
            r2, c2 = r + step * dr, c + step * dc
            if 1 <= r2 <= N and 1 <= c2 <= N:
                moves.append(gen_one_moves(r, c, step, dr, dc))
    return moves


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        M = []
        n = len(pieces)
        for i in range(n):
            p = pieces[i]
            r, c = positions[i]
            M.append(gen_moves(r, c, p))

        # print(len(M[0]), len(M[1]))

        def dfs(sel):
            if len(sel) == n:
                probeN = max(len(x) for x in sel)

                for probe in range(probeN):
                    s = set()
                    for i in range(n):
                        if probe < len(sel[i]):
                            s.add(sel[i][probe])
                        else:
                            s.add(sel[i][-1])
                    if len(s) != n:
                        return 0
                return 1

            k = len(sel)
            ans = 0
            for moves in M[k]:
                sel.append(moves)
                ans += dfs(sel)
                sel.pop()
            return ans

        ans = dfs([])
        return ans


true, false, null = True, False, None
cases = [
    (["rook"], [[1, 1]], 15),
    (["queen"], [[1, 1]], 22),
    (["bishop"], [[4, 3]], 12),
    (["rook", "rook"], [[1, 1], [8, 8]], 223),
    (["queen", "bishop"], [[5, 7], [3, 4]], 281),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countCombinations, cases)

if __name__ == '__main__':
    pass
