#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        stack = []
        pairs = ('[{(', ']})')
        matched = True
        for s in expression:
            if s in pairs[0]:
                stack.append(s)
                continue
            idx = pairs[1].find(s)
            if (not stack) or (stack[-1] != pairs[0][idx]):
                matched = False
                break
            stack.pop()
        if matched and stack:
            matched = False
        if matched:
            print('YES')
        else:
            print('NO')
