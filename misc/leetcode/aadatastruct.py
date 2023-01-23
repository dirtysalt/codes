#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import math


class UnionFind:
    def __init__(self, values):
        r, c, = {}, {}
        for v in values:
            r[v], c[v] = v, 1
        self.r, self.c = r, c

    def size(self, a):
        ra = self.find(a)
        return self.c[ra]

    def find(self, a):
        if a not in self.r:
            self.r[a] = a
            self.c[a] = 1
            return a

        # find root.
        x = a
        while True:
            ra = self.r[x]
            if ra == x:
                break
            x = ra

        # compress path.
        x = a
        while x != ra:
            rx = self.r[x]
            self.r[x] = ra
            x = rx
        return ra

    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        ca, cb = self.c[ra], self.c[rb]
        if ca > cb:
            ca, cb, ra, rb = cb, ca, rb, ra
        self.r[ra] = rb
        self.c[rb] += ca


class StringHashBuilder:
    BASE = 13131
    MOD = 151217133020331712151
    # OFFSET = ord('a')
    OFFSET = 96

    def __init__(self, s):
        n = len(s)
        self.hash = [0] * (n + 1)
        self.base = [0] * (n + 1)
        self.base[0] = b = 1
        self.hash[0] = h = 0
        for i in range(n):
            h = (h * self.BASE + ord(s[i]) - self.OFFSET) % self.MOD
            b = (b * self.BASE) % self.MOD
            self.hash[i + 1] = h
            self.base[i + 1] = b

    def getHash(self, left, right):
        upper = self.hash[right]
        lower = (self.hash[left] * self.base[right - left]) % self.MOD
        return (upper - lower + self.MOD) % self.MOD


class PrefixSumTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (n + 1)
        self.n = n
        for i in range(n):
            self.updateSum(i, arr[i])

    def getSum(self, index):
        t = 0
        index = index + 1
        while index > 0:
            t += self.tree[index]
            index -= index & (-index)
        return t

    def updateSum(self, index, val):
        index = index + 1
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)


def mat_mul(a, b, MOD):
    R, K, C = len(a), len(a[0]), len(b[0])
    res = [[0] * C for _ in range(R)]
    for k in range(K):
        for i in range(R):
            for j in range(C):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
                res[i][j] %= MOD
    return res


class StreamStatistics:
    def __init__(self):
        self.sum = 0
        self.n = 0
        self.x2 = 0

    def add(self, x):
        self.sum += x
        self.n += 1
        self.x2 += x * x

    def rem(self, x):
        self.sum -= x
        self.n -= 1
        self.x2 -= x * x

    def avg(self):
        return self.sum / self.n

    def dev(self):
        m = self.avg()
        t = self.x2 - self.sum * self.sum / self.n
        return t / self.n


class GeometryUtil:
    @staticmethod
    def TwoLinesCrossPoint(line1, line2, onLine=True):
        # https://zhuanlan.zhihu.com/p/138718555
        point_is_exist = False
        x = y = 0
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2

        if (x2 - x1) == 0:
            k1 = None
            b1 = 0
        else:
            k1 = (y2 - y1) * 1.0 / (x2 - x1)  # 计算k1,由于点均为整数，需要进行浮点数转化
            b1 = y1 * 1.0 - x1 * k1 * 1.0  # 整型转浮点型是关键

        if (x4 - x3) == 0:  # L2直线斜率不存在
            k2 = None
            b2 = 0
        else:
            k2 = (y4 - y3) * 1.0 / (x4 - x3)  # 斜率存在
            b2 = y3 * 1.0 - x3 * k2 * 1.0

        if k1 is None:
            if not k2 is None:
                x = x1
                y = k2 * x1 + b2
                point_is_exist = True
        elif k2 is None:
            x = x3
            y = k1 * x3 + b1
        elif not k2 == k1:
            x = (b2 - b1) * 1.0 / (k1 - k2)
            y = k1 * x * 1.0 + b1 * 1.0
            point_is_exist = True

        if point_is_exist:
            p = [x, y]
            if onLine and GeometryUtil.PointOnLine(p, line1, line2):
                return [x, y]
        return []

    @staticmethod
    def PointOnLine(p, l, l2):
        x, y = p
        x1, y1, x2, y2 = l
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return []
        x1, y1, x2, y2 = l2
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return []
        return p

    @staticmethod
    def LineIntersectCircle(p, l):
        # https://www.codingdict.com/questions/187334
        x0, y0, r0 = p
        x1, y1, x2, y2 = l
        if x1 == x2:
            if abs(r0) >= abs(x1 - x0):
                p1 = x1, y0 - math.sqrt(r0 ** 2 - (x1 - x0) ** 2)
                p2 = x1, y0 + math.sqrt(r0 ** 2 - (x1 - x0) ** 2)
                inp = [p1, p2]
                # select the points lie on the line segment
                inp = [p for p in inp if min(y1, y2) <= p[1] <= max(y1, y2)]
            else:
                inp = []
        else:
            k = (y1 - y2) / (x1 - x2)
            b0 = y1 - k * x1
            a = k ** 2 + 1
            b = 2 * k * (b0 - y0) - 2 * x0
            c = (b0 - y0) ** 2 + x0 ** 2 - r0 ** 2
            delta = b ** 2 - 4 * a * c
            if delta >= 0:
                p1x = (-b - math.sqrt(delta)) / (2 * a)
                p2x = (-b + math.sqrt(delta)) / (2 * a)
                p1y = k * x1 + b0
                p2y = k * x2 + b0
                inp = [[p1x, p1y], [p2x, p2y]]
                # select the points lie on the line segment
                inp = [p for p in inp if min(x1, x2) <= p[0] <= max(x1, x2)]
            else:
                inp = []
        return inp

    @staticmethod
    def TwoCirclesCrossPoint(p1, p2):
        x, y, R = p1
        a, b, S = p2
        d = math.sqrt((abs(a - x)) ** 2 + (abs(b - y)) ** 2)
        if d > (R + S) or d < (abs(R - S)):
            # print("Two circles have no intersection")
            return []
        elif d == 0 and R == S:
            # print("Two circles have same center!")
            return []
        else:
            A = (R ** 2 - S ** 2 + d ** 2) / (2 * d)
            h = math.sqrt(R ** 2 - A ** 2)
            x2 = x + A * (a - x) / d
            y2 = y + A * (b - y) / d
            x3 = x2 - h * (b - y) / d
            y3 = y2 + h * (a - x) / d
            x4 = x2 + h * (b - y) / d
            y4 = y2 - h * (a - x) / d
            return [x3, y3, x4, y4]


class RangeOp:
    def __init__(self, iv, fn):
        self.iv = iv
        self.fn = fn

    @staticmethod
    def MaxOp():
        return RangeOp(0, lambda x, y: max(x, y))

    @staticmethod
    def SumOp():
        return RangeOp(0, lambda x, y: x + y)


class RangeTree:
    def __init__(self, sz, op: RangeOp):
        n = 1
        while n < sz:
            n = n * 2
        self.n = n
        self.sz = sz
        self.values = [op.iv] * (2 * n)
        self.op = op

    def update(self, idx, x):
        off = self.n + idx
        self.values[off] = x
        while off > 1:
            p = off // 2
            self.values[p] = self.op.fn(self.values[2 * p], self.values[2 * p + 1])
            off = p

    def top(self):
        return self.values[1]

    def get(self, idx):
        return self.values[idx + self.n]

    def query(self, a, b):
        def search(p, off, size):
            x, y = off, off + size - 1
            if x >= a and y <= b:
                return self.values[p]
            if x > b or y < a:
                return 0

            half = size // 2
            vx = search(2 * p, off, half)
            vy = search(2 * p + 1, off + half, half)
            return self.op.fn(vx, vy)

        return search(1, 0, self.n)


if __name__ == '__main__':
    pass
