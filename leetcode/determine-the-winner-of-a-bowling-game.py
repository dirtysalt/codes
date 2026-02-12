#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(arr):
            ans = 0
            for i in range(len(arr)):
                ans += arr[i]
                if (i >= 1 and arr[i - 1] == 10) or (i >= 2 and arr[i - 2] == 10):
                    ans += arr[i]
            return ans

        ans = 0
        a, b = score(player1), score(player2)
        if a > b:
            ans = 1
        elif a < b:
            ans = 2
        return ans


if __name__ == '__main__':
    pass
