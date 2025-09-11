#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = [(x - y, idx) for idx, (x, y) in enumerate(zip(reward1, reward2))]
        diff.sort(reverse=True)

        ans = 0
        for _, idx in diff[:k]:
            ans += reward1[idx]
        for _, idx in diff[k:]:
            ans += reward2[idx]
        return ans


if __name__ == '__main__':
    pass
