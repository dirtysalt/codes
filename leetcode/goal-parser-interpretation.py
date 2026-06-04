#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def interpret(self, command: str) -> str:
        tmp = []
        i = 0
        while i < len(command):
            c = command[i]
            if c == 'G':
                tmp.append('G')
            elif c == '(':
                c2 = command[i + 1]
                if c2 == ')':
                    tmp.append('o')
                    i += 1
                else:
                    tmp.append('al')
                    i += 3
            i += 1
        ans = ''.join(tmp)
        return ans

