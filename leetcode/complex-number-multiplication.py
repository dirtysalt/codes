#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def parse(s):
            real = 0
            imag = 0
            i = 0

            neg = False
            if s[i] == '-':
                i += 1
                neg = True
            while s[i] != '+':
                real = real * 10 + int(s[i])
                i += 1
            if neg:
                real = -real

            i += 1
            neg = False
            if s[i] == '-':
                i += 1
                neg = True
            while s[i] != 'i':
                imag = imag * 10 + int(s[i])
                i += 1
            if neg:
                imag = -imag
            return real, imag

        ra, ia = parse(a)
        rb, ib = parse(b)
        rc = ra * rb - ia * ib
        ic = ra * ib + ia * rb
        s = '{}+{}i'.format(rc, ic)
        return s
