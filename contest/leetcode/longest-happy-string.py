#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        xs = [('a', a), ('b', b), ('c', c)]
        st = []

        changed = True
        while changed:
            changed = False
            xs.sort(key=lambda x: x[1], reverse=True)
            for idx, (k, v) in enumerate(xs):
                if v == 0:
                    continue
                if len(st) >= 2 and st[-1] == k and st[-2] == k:
                    continue

                changed = True
                st.append(k)
                xs[idx] = (k, v - 1)
                break

        ans = ''.join(st)
        return ans