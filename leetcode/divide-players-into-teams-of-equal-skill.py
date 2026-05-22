#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        i, j = 0, n - 1
        exp = skill[i] + skill[j]
        ans = 0
        while i < j:
            z = skill[i] + skill[j]
            if z != exp:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans


if __name__ == '__main__':
    pass
