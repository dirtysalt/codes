#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and s[i] == '1': i += 1
        while i < n and s[i] == '0': i += 1
        if i == n: return True
        return False
