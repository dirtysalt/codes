#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
In general situation, it should be transformed into a problem to calculate A from AX=B, matrix X is formed as follows,
         //                                             /// efghinorstuvwxz ///
        // 0 z e r o        e         o  r            z    100000110000001
        // 1 o n e          e        no                    100001100000000
        // 2 t w o                    o      t    w         000000100100100
        // 3 t h r e e      e    h       r   t              200100010100000
        // 4 f o u r          f       o  r     u             010000110010000
        // 5 f i v e        e f    i             v            110010000001000
        // 6 s i x                 i       s        x          000010001000010
        // 7 s e v e n      e        n     s     v        200001001001000
        // 8 e i g h t      e  g h i         t              101110000100000
        // 9 n i n e        e      i n                       100012000000000
"""


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        def ch2idx(c):
            return ord(c) - ord('a')

        counter = [0] * 26
        for c in s:
            idx = ch2idx(c)
            counter[idx] += 1

        preps = []
        for word in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            vec = []
            for c in word:
                vec.append(ch2idx(c))
            preps.append(vec)

        def remove_chars(c, digit):
            idx = ch2idx(c)
            prep = preps[digit]
            cnt = counter[idx]
            for idx in prep:
                counter[idx] -= cnt
            return str(digit) * cnt

        res = ''
        res += remove_chars('z', 0)
        res += remove_chars('x', 6)
        res += remove_chars('w', 2)
        res += remove_chars('u', 4)
        res += remove_chars('g', 8)
        res += remove_chars('o', 1)
        res += remove_chars('h', 3)
        res += remove_chars('f', 5)
        res += remove_chars('v', 7)
        res += remove_chars('i', 9)
        res = list(res)
        res.sort()
        res = ''.join(res)
        return res
