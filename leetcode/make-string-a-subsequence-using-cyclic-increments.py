#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)

        m = {}
        for i in range(25):
            m[chr(i + ord('a'))] = chr(i + 1 + ord('a'))
        m['z'] = 'a'
        # print(m)

        i = 0
        for c in str2:
            while i < n:
                if str1[i] == c or m[str1[i]] == c:
                    break
                i += 1
            # print(i,n)
            if i == n:
                return False
            i += 1
        return True


if __name__ == '__main__':
    pass
