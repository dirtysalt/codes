#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)

        def cons(c):
            ans = 0
            sz = 0
            for i in range(n):
                if colors[i] == c:
                    sz += 1
                else:
                    if sz >= 3:
                        ans += sz - 2
                    sz = 0
            if sz >= 3:
                ans += sz - 2
            return ans

        A = cons('A')
        B = cons('B')
        # print(A, B)
        if A > B:
            return True
        return False


if __name__ == '__main__':
    pass
