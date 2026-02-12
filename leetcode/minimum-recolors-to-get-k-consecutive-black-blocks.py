#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        ans = w
        for i in range(k, n):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            ans = min(ans, w)
        return ans


if __name__ == '__main__':
    pass
