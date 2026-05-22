#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def opA(s, a):
            ss = [int(x) for x in s]
            for i in range(len(ss)):
                if i % 2 == 1:
                    ss[i] = (ss[i] + a) % 10
            return ''.join((str(x) for x in ss))

        def opB(s, b):
            return s[-b:] + s[:-b]

        ss = set()
        from collections import deque
        dq = deque()
        dq.append(s)
        ss.add(s)
        ans = s
        while dq:
            s = dq.pop()
            ans = min(ans, s)
            sa = opA(s, a)
            sb = opB(s, b)
            # print(s, s2, s3)
            if sa not in ss:
                ss.add(sa)
                dq.append(sa)
            if sb not in ss:
                ss.add(sb)
                dq.append(sb)
        return ans
