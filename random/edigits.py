#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from __future__ import (absolute_import, division, print_function, unicode_literals)

def compute_exp(scale):
    scale_10 = 10 ** scale
    fac = 1
    fac_thres = scale_10 * 100
    a = scale_10
    b = 0
    i = 0
    while True:
        i += 1
        fac *= i
        if fac >= fac_thres:
            break
        a += scale_10 // fac
        b += scale_10 % fac

    a += b // scale_10
    b = b % scale_10
    return (a, b)
