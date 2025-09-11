#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from collections import Counter
        color = {}
        cnt = Counter()
        ans = []
        for x, y in queries:
            py = color.get(x)
            if py is not None:
                cnt[py] -= 1
                if cnt[py] == 0:
                    del cnt[py]
            color[x] = y
            cnt[y] += 1
            ans.append(len(cnt))
        return ans


if __name__ == '__main__':
    pass
