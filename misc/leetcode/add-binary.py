#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        f = 0
        a = a[::-1]
        b = b[::-1]
        n = max(len(a), len(b))
        res = [0] * n
        for i in range(0, n):
            f += (int(a[i]) if i < len(a) else 0) + \
                 (int(b[i]) if i < len(b) else 0)
            res[i] = f & 0x1
            f = f >> 1
        if f: res.append(f)
        return ''.join(map(str, reversed(res)))


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('111', '10'))
