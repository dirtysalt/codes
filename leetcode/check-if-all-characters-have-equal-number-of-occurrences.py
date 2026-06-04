#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occ = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            occ[i] += 1

        rep = 0
        for x in occ:
            if x != 0:
                if rep == 0:
                    rep = x
                elif rep != x:
                    return False
        return True


if __name__ == '__main__':
    pass
