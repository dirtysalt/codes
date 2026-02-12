#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        n, m = len(board), len(board[0])

        def toint(c):
            if c == 'W':
                return 0
            elif c == 'B':
                return 1
            else:
                return -1

        delta = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0: continue
                delta.append((i, j))

        def check(buf):
            rep = 0
            for i in range(1, len(buf)):
                if buf[i] == buf[0]:
                    if rep >= 1:
                        return True
                    return False

                if buf[i] == (1 - buf[0]):
                    rep += 1
                    continue
                else:
                    break

            return False

        for dx, dy in delta:
            buf = []
            i, j = rMove, cMove
            board[i][j] = color
            while 0 <= i < n and 0 <= j < m:
                buf.append(toint(board[i][j]))
                i += dx
                j += dy
            # print(buf)
            if check(buf):
                return True

        return False


true, false, null = True, False, None
cases = [
    ([[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
      [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
      ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."],
      [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], 4, 3, 'B', True),
    ([[".", ".", "W", ".", "B", "W", "W", "B"], ["B", "W", ".", "W", ".", "W", "B", "B"],
      [".", "W", "B", "W", "W", ".", "W", "W"], ["W", "W", ".", "W", ".", ".", "B", "B"],
      ["B", "W", "B", "B", "W", "W", "B", "."], ["W", ".", "W", ".", ".", "B", "W", "W"],
      ["B", ".", "B", "B", ".", ".", "B", "B"], [".", "W", ".", "W", ".", "W", ".", "W"]],
     5, 4, 'W', True),
    ([[".", ".", ".", ".", ".", ".", ".", "."], [".", "B", ".", ".", "W", ".", ".", "."],
      [".", ".", "W", ".", ".", ".", ".", "."], [".", ".", ".", "W", "B", ".", ".", "."],
      [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "B", "W", ".", "."],
      [".", ".", ".", ".", ".", ".", "W", "."], [".", ".", ".", ".", ".", ".", ".", "B"]]
     , 4, 4, 'W', False),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkMove, cases)

if __name__ == '__main__':
    pass
