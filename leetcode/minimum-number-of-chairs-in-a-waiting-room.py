#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s:
            if c == 'E':
                cnt += 1
            else:
                cnt -= 1
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    pass
