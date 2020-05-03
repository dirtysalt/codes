#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = []

        def fx(s, off, p, r):
            if p == 4 or off == len(s):
                if p == 4 and off == len(s):
                    res.append('.'.join([str(x) for x in r]))
                return

            if s[off] == '0':
                r.append(0)
                fx(s, off + 1, p + 1, r)
                r.pop()
                return

            v = 0
            for i in range(off, len(s)):
                v = v * 10 + int(s[i])
                if v < 256:
                    r.append(v)
                    fx(s, i + 1, p + 1, r)
                    r.pop()

        r = []
        fx(s, 0, 0, r)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('25525511135'))
    print(s.restoreIpAddresses('1111'))
    print(s.restoreIpAddresses('0000'))
    print(s.restoreIpAddresses('00000'))
