#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        from collections import Counter
        cnt = Counter()
        taken = set()

        ans = []
        for x in names:
            idx = cnt[x]

            while True:
                res = x
                if idx != 0:
                    res = x + '(%d)' % (idx)
                if res not in taken:
                    break
                idx += 1

            cnt[x] = idx + 1
            taken.add(res)
            ans.append(res)
        return ans
