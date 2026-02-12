#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    ans -= 1
                    break
        return ans


if __name__ == '__main__':
    pass
