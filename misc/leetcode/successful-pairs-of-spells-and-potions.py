#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for x in spells:
            exp = success // x
            if exp * x < success:
                exp += 1
            s, e = 0, len(potions) - 1
            while s <= e:
                m = (s + e) // 2
                if potions[m] < exp:
                    s = m + 1
                else:
                    e = m - 1
            ans.append(len(potions) - s)

        return ans


if __name__ == '__main__':
    pass
