#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(26):
            ps = []
            for j in range(len(s)):
                if i == (ord(s[j]) - ord('a')):
                    ps.append(j)
            if ps and (ps[1] - ps[0]) != (distance[i] + 1):
                return False
        return True


if __name__ == '__main__':
    pass
