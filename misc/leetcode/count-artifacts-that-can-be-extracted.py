#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        digs = set()
        for r, c in dig:
            digs.add((r, c))

        ans = 0
        for r0, c0, r1, c1 in artifacts:
            ok = True
            for x in range(r0, r1 + 1):
                for y in range(c0, c1 + 1):
                    if (x, y) not in digs:
                        ok = False
                        break
                if not ok: break
            if ok:
                ans += 1

        return ans

if __name__ == '__main__':
    pass
