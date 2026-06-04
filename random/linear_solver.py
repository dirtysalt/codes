#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

import numpy as np
from scipy import optimize as op


def test(maxAdjustRatio=None):
    print('=====' + str(maxAdjustRatio) + '=====')
    old_ratio = np.array([3.20, 3.20, 3.20, 3.20, 10.80, 10.80, 2.20, 27.60, 28.80, 1.60]) * 0.01

    # 定义目标函数系数
    # 股票资产占比
    C = np.array([0.365, 0.235, 0.176, 0.298, 0.17, 0.255, 0.001, 0, 0, 0])
    n = len(C)

    T = 184000  # 规模
    R = 0.1  # 股票比例
    T2 = 500  # 冻结
    CASH_RATIO = 0.054  # 现金比例

    # 实际剩余基金大小
    CT = (T - T2) * (1 - CASH_RATIO)

    if np.sum(old_ratio * C) > R:
        print("bad old ratio")
        return False

    # 定义约束条件系数
    AUB = [
        C.copy(),
    ]
    BUB = [
        T * R,
    ]

    AEQ = [
        np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        np.array([1, -1, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([1, 0, -1, 0, 0, 0, 0, 0, 0, 0]),
        np.array([1, 0, 0, -1, 0, 0, 0, 0, 0, 0]),
        np.array([1, 0, 0, 0, 0, -1, 0, 0, 0, 0]),
    ]

    BEQ = [
        CT, 0, 0, 0, 0
    ]

    BOUNDS = [(0, None)] * n
    if maxAdjustRatio is not None:

        C = np.append(C, np.zeros(n))
        for i in range(len(AUB)):
            AUB[i] = np.append(AUB[i], np.zeros(n))
        for i in range(len(AEQ)):
            AEQ[i] = np.append(AEQ[i], np.zeros(n))
        BOUNDS.extend([(0, None)] * n)

        # introduce other variables.
        norm = old_ratio / np.sum(old_ratio)
        n2 = 2 * n
        for i in range(n):
            old = norm[i] * CT

            # abs(c-old)
            # absx >= c-old
            # -absx + c <= old
            a = [0] * n2
            a[i] = 1
            a[i + n] = -1
            b = old
            AUB.append(a)
            BUB.append(b)

            # absx >= -(c-old)
            # -absx <= (c-old)
            # -absx -c <= -old
            a = [0] * n2
            a[i] = -1
            a[i + n] = -1
            b = -old
            AUB.append(a)
            BUB.append(b)

        a = [0] * n2
        for i in range(n):
            a[i + n] = 1
        b = maxAdjustRatio * CT
        AUB.append(a)
        BUB.append(b)

    # 求解
    res = op.linprog(-C, A_ub=np.array(AUB), b_ub=np.array(BUB), A_eq=np.array(AEQ),
                     b_eq=np.array(BEQ),
                     bounds=BOUNDS)
    if not res.success:
        return False

    print(res)
    x = res.x

    if maxAdjustRatio is not None:
        x = x[:n]

    ratio = np.round(x / np.sum(x), 3)
    print('max adjust = {}'.format(maxAdjustRatio))
    print('old ratio = {}'.format(old_ratio))
    print('new ratio = {}'.format(ratio))
    print('abs adjust = {}'.format(np.sum(np.abs(ratio - old_ratio))))
    return True


def run():
    test()
    for maxAdjustRatio in (0.1, 0.12, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35):
        if test(maxAdjustRatio):
            break


if __name__ == '__main__':
    run()
