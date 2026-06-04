#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        cnt.sort(reverse=True)
        ans = sum(cnt[k:])
        return ans


if __name__ == '__main__':
    pass
