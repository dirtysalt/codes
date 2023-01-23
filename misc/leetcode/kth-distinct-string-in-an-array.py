#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        cnt = Counter(arr)

        t = k
        for x in arr:
            if cnt[x] == 1:
                t -= 1
                if t == 0:
                    return x

        return ""


if __name__ == '__main__':
    pass
