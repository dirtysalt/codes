#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt = [0] * 26

        sizes = []
        for w in words:
            for c in w:
                c2 = ord(c) - ord('a')
                cnt[c2] += 1
            sizes.append(len(w))

        sizes.sort()

        def match(sz, cnt):
            n = sz // 2
            tmp = cnt.copy()
            for i in range(26):
                x = min(tmp[i] // 2, n)
                tmp[i] -= 2 * x
                n -= x
                if n == 0: break
            if n != 0: return False, cnt
            if sz % 2 == 0: return True, tmp

            for i in range(26):
                if tmp[i] % 2 == 1:
                    tmp[i] -= 1
                    return True, tmp
            for i in range(26):
                if tmp[i] > 0:
                    tmp[i] -= 1
                    return True, tmp
            return False, cnt

        ans = 0
        for sz in sizes:
            ok, cnt = match(sz, cnt)
            if ok: ans += 1
        return ans


if __name__ == '__main__':
    pass
