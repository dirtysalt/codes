#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = 0
        for c in s:
            if c in 'aeiuo':
                cnt += 1
        return True if cnt > 0 else False


if __name__ == '__main__':
    pass
