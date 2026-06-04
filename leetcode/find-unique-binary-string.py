#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set()
        for w in nums:
            v = 0
            for c in w:
                x = ord(c) - ord('0')
                v = v * 2 + x
            seen.add(v)

        # print(seen)
        ans = []
        for x in range(1 << n):
            if x in seen: continue
            for i in reversed(range(n)):
                if (x >> i) & 0x1:
                    ans.append('1')
                else:
                    ans.append('0')
            return ''.join(ans)


if __name__ == '__main__':
    pass
