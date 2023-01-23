#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        # build transfer state
        res = []
        tmp = []
        length = 0
        res.append(('', 0))
        for s in S:
            if s in '0123456789':
                d = int(s)
                length += len(tmp)
                length *= d
                res.append((tmp, length))
                tmp = []
            else:
                tmp.append(s)
        if tmp:
            length += len(tmp)
            res.append((tmp, length))

        # decode in reversed order.
        n = len(res)
        K = K - 1
        for i in range(n - 1, 0, -1):
            length = (res[i - 1][1] + len(res[i][0]))
            idx = K % length
            if idx >= res[i - 1][1]:
                return res[i][0][idx - res[i - 1][1]]
            else:
                K = idx
        return None
