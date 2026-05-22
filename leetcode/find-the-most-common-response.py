#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        from collections import Counter
        cnt = Counter()
        max_occ = 0
        for r in responses:
            for x in set(r):
                cnt[x] += 1
                max_occ = max(max_occ, cnt[x])

        ans = None
        for k, v in cnt.items():
            if v == max_occ:
                if ans is None or k < ans:
                    ans = k
        return ans


if __name__ == '__main__':
    pass
