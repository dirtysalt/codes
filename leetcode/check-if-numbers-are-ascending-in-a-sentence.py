#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = -1
        i = 0

        while i < len(s):
            c = ord(s[i]) - ord('0')
            if 0 <= c <= 9:
                res = 0
                while i < len(s):
                    c = ord(s[i]) - ord('0')
                    i += 1
                    if 0 <= c <= 9:
                        res = res * 10 + c
                    else:
                        break
                if res <= last:
                    return False
                last = res
            else:
                i += 1
        return True


if __name__ == '__main__':
    pass
