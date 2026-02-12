#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            c2 = ord(c) - ord('a')
            cnt[c2] += 1

        ans = 0
        for x in cnt:
            if x >= 2: x = 1
            ans += x
        return ans


if __name__ == '__main__':
    pass
