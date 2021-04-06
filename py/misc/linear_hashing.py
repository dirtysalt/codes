#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq
import numpy as np

simplehash = hash

import mmh3
def simplehash(key):
    return mmh3.hash(key, signed = False)

class LinearHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def __repr__(self):
        return 'LH(size=%d,count=%d,table=%s)' % (self.size, self.count, self.table)

    def add(self, key, value):
        if self.count == self.size:
            return False
        self.count += 1

        start = pos = key % self.size
        offset = 0
        while self.table[pos] is not None:
            pos = (pos + 1) % self.size
            offset += 1
        self.table[pos] = (key, value, offset)
        return True

    def query(self, key):
        start = pos = key % self.size
        step = 0
        while self.table[pos] is not None:
            (k, v, off) = self.table[pos]
            if key == k:
                assert(step == off)
                return v, off
            pos = (pos + 1) % self.size
            step += 1
            if pos == start:
                return None
        return None

class RobinHoodHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def __repr__(self):
        return 'RH(size=%d,count=%d,table=%s)' % (self.size, self.count, self.table)

    def add(self, key, value):
        if self.count == self.size:
            return False
        self.count += 1

        start = pos = key % self.size
        offset = 0
        while self.table[pos] is not None:
            (k, v, off) = self.table[pos]
            if offset > off:
                # 站住这个地方，将原来的内容置换出来
                self.table[pos] = (key, value, offset)
                key, value, offset = k, v, off + 1
            else:
                # 去下个地方查找
                offset += 1
            pos = (pos + 1) % self.size
        self.table[pos] = (key, value, offset)
        return True

    def query(self, key):
        start = pos = key % self.size
        step = 0
        while self.table[pos] is not None:
            (k, v, off) = self.table[pos]
            if key == k:
                assert(step == off)
                return v, off
            pos = (pos + 1) % self.size
            step += 1
            if pos == start:
                return None
        return None

import unittest
class TestAll(unittest.TestCase):
    def test_hashing(self):
        size = 512 - 1
        rhh = RobinHoodHashing(size)
        lnh = LinearHashing(size)

        # 随着load越来越大，可以看到linear分布越来越不均匀
        # 但是即便如此，在p90上依然比robinhood要好
        # 这让我比较怀疑robin hood的实用性
        num = int(size * 0.8)
        keys = set()
        for data in range(num):
            key = simplehash("key" + str(data))
            self.assertTrue(key not in keys)
            keys.add(key)
            self.assertTrue(rhh.add(key, data))
            self.assertTrue(lnh.add(key, data))

        rhh_offset = []
        lnh_offset = []
        for data in range(num):
            key = simplehash("key" + str(data))
            ret = rhh.query(key)
            self.assertTrue(ret is not None)
            value, off = ret
            rhh_offset.append(off)
            self.assertEqual(value, data)

            ret = lnh.query(key)
            self.assertTrue(ret is not None)
            value, off = ret
            lnh_offset.append(off)
            self.assertEqual(value, data)


        print('=====RHH and LNH offset data=====')
        print(rhh_offset)
        print(lnh_offset)
        for p in (50, 75, 90, 95, 99):
            print("robin hood p%d offset = %.2f" % (p, np.percentile(rhh_offset, p)))
            print("linear p%d offset = %.2f" % (p, np.percentile(lnh_offset, p)))


def debug():
    print('=====RobinHood=====')
    rhh = RobinHoodHashing(13)
    items = [(0, 9), (1, 10), (14, 11), (27, 12), (13, 13)]
    for k, v in items:
        print('add (%d, %d)' % (k, v))
        rhh.add(k, v)
        print(rhh)

    print('=====Linear=====')
    lnh = LinearHashing(13)
    items = [(0, 9), (1, 10), (14, 11), (27, 12), (13, 13)]
    for k, v in items:
        print('add (%d, %d)' % (k, v))
        lnh.add(k, v)
        print(lnh)


if __name__ == '__main__':
    debug()
    unittest.main()
