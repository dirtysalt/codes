#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        v = 1
        for i in range(1, n):
            v = self.next_value(v)
            print(v)
        return str(v)

    def next_value(self, n):
        ints = []
        prev = None
        cnt = 0
        while n:
            v = n % 10
            n = n / 10
            if v != prev:
                if prev is not None:
                    ints.append((prev, cnt))
                prev = v
                cnt = 1
            else:
                cnt += 1
        if prev:
            ints.append((prev, cnt))
        s = ''
        for (v, cnt) in ints:
            s = '%d%d' % (cnt, v) + s
        return int(s)


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(10))
