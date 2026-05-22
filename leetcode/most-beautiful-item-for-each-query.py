#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = [tuple(x) for x in items]
        items.sort()
        st = []
        for x in items:
            if st:
                if st[-1][1] >= x[1]:
                    pass
                elif st[-1][0] == x[0]:
                    st[-1] = x
                else:
                    st.append(x)
            else:
                st.append(x)

        # print(items, st)
        ans = []
        for q in queries:
            s, e = 0, len(st) - 1
            while s <= e:
                m = (s + e) // 2
                if st[m][0] > q:
                    e = m - 1
                else:
                    s = m + 1
            if e == -1:
                ans.append(0)
            else:
                ans.append(st[e][1])
        return ans


if __name__ == '__main__':
    pass
