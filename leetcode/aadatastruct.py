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

    def get_hash(self, left, right):
        upper = self.hash[right]
        lower = (self.hash[left] * self.base[right - left]) % self.MOD
        return (upper - lower + self.MOD) % self.MOD


class PrefixSumTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (n + 1)
        self.n = n
        for i in range(n):
            self.update_sum(i, arr[i])

    def get_sum(self, index):
        t = 0
        index = index + 1
        while index > 0:
            t += self.tree[index]
            index -= index & (-index)
        return t

    def update_sum(self, index, val):
        index = index + 1
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)


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


def two_lines_cross_point(line1, line2, on_the_line=True):
    """求解两条线的交点"""
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

    def is_point_on_line(p, l, l2):
        x, y = p
        x1, y1, x2, y2 = l
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return False
        x1, y1, x2, y2 = l2
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return False
        return True

    if point_is_exist:
        p = [x, y]
        if on_the_line and is_point_on_line(p, line1, line2):
            return [x, y]
    return []


def line_intersect_circle(p, l):
    """求解圆和直线的交点"""
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


def two_circles_cross_point(p1, p2):
    """求解两个圆之间的交点"""
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
    def max():
        return RangeOp(0, lambda x, y: max(x, y))

    @staticmethod
    def sum():
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


class SegmentTreeSummer:
    class Base:
        def __init__(self, n):
            self.values = [0] * n

        def update(self, i, j, delta):
            for k in range(i, j + 1):
                self.values[k] += delta

        def query(self, i, j):
            acc = 0
            for k in range(i, j + 1):
                acc += self.values[k]
            return acc

    def __init__(self, n):
        self.n = n
        sz = 1
        while sz < n:
            sz <<= 1
        self.sum = [0] * (sz << 1)
        self.lazy = [0] * (sz << 1)
        self.sz = sz
        self.base = SegmentTreeSummer.Base(n)
        self.debug = False

    def dump(self):
        sz = 1
        off = 1
        while sz <= self.sz:
            print(self.sum[off:off + sz], self.lazy[off:off + sz])
            off += sz
            sz = sz << 1

    def query_and_update(self, i, j, delta):
        def do(i, j, k, s, sz):

            if i <= s <= (s + sz - 1) <= j:
                res = self.sum[k]
                self.apply_lazy(k, sz, delta)
                return res

            self.push_down(k, sz)
            mid = s + sz // 2
            res = 0
            if i < mid:
                res += do(i, j, 2 * k, s, sz // 2)
            if j >= mid:
                res += do(i, j, 2 * k + 1, mid, sz // 2)

            self.sum[k] = self.sum[2 * k] + self.sum[2 * k + 1]
            return res

        ans = do(i, j, 1, 0, self.sz)
        if self.debug:
            exp = self.base.query(i, j)
            self.base.update(i, j, delta)
            print('query_and_update(%d, %d) = %d' % (i, j, ans))
            self.dump()

            if ans != exp:
                assert (ans == exp)
        return ans

    def push_down(self, k, sz):
        if self.lazy[k] and sz != 1:
            v = self.lazy[k]
            self.apply_lazy(2 * k, sz // 2, v)
            self.apply_lazy(2 * k + 1, sz // 2, v)
            self.lazy[k] = 0

    def apply_lazy(self, k, sz, delta):
        self.sum[k] += delta * sz
        self.lazy[k] += delta

    def query(self, i, j):
        return self.query_and_update(i, j, 0)

    def update(self, i, j, delta):
        self.query_and_update(i, j, delta)


def tarjan_lca(graph, root, queries):
    class UnionFindSet:
        def __init__(self, n):
            self.ps = [0] * n
            for i in range(n):
                self.ps[i] = i

        def find(self, x):
            p = x
            while self.ps[p] != p:
                p = self.ps[p]

            while self.ps[x] != x:
                up = self.ps[x]
                self.ps[x] = p
                x = up
            return p

        def set(self, x, p):
            self.ps[x] = p

    from collections import defaultdict
    query_index = defaultdict(list)
    ans = [-1] * len(queries)
    for idx, (u, v) in enumerate(queries):
        query_index[u].append((v, idx))
        query_index[v].append((u, idx))

    n = len(graph)
    ufs = UnionFindSet(n)
    visited = [0] * n

    def dfs(root, parent):
        # answer queries.
        visited[root] = 1
        query = query_index[root]
        for v, idx in query:
            # 如果这个节点之前没有被访问过，那么是不知道LCA的
            if not visited[v]: continue
            # 如果有对应的查询节点v, 并且这个节点之前访问过
            # 那么使用这个节点的parent.
            # 如果v是root的祖先节点的话，那么就是v
            # 如果v在另外一个树上的话，那么就是最早交汇的节点
            p = ufs.find(v)
            ans[idx] = p

        # continue to dfs.
        for v, _ in graph[root]:
            if v != parent:
                dfs(v, root)
                # 遍历子节点之后，将子节点的父节点设置为自己
                ufs.set(v, root)

    dfs(root, -1)
    return ans


def get_primes(N):
    ps = []
    mask = [0] * (N + 1)
    for i in range(2, N + 1):
        if mask[i] == 1: continue
        for j in range(2, N + 1):
            if i * j > N: break
            mask[i * j] = 1
    for i in range(2, N + 1):
        if mask[i] == 0:
            ps.append(i)
    return ps


# 费马小定理, 但是这里必须确保MOD是质数
# b^MOD % MOD = b
# b^(MOD-1) % MOD = 1
# b^(MOD-2) % MOD = (b^-1) % MOD
def pow_mod(a, b, MOD):
    res = 1
    while b:
        if b & 0x1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b = b >> 1
    return res


#
def div_mod(b, MOD):
    return pow_mod(b, MOD - 2, MOD)


# 相比费马小定理，这里不要求MOD是质数，只需要确保b和MOD是互质就行
# b * x + MOD * y =  1(% MOD)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y


def mod_inverse(b, MOD):
    d, x, y = extended_gcd(b, MOD)
    assert (d == 1)
    return x % MOD


def mat_mul(a, b, MOD):
    R, K, C = len(a), len(a[0]), len(b[0])
    res = [[0] * C for _ in range(R)]
    for k in range(K):
        for i in range(R):
            for j in range(C):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
                res[i][j] %= MOD
    return res


class KMP:
    @staticmethod
    def build_max_match(t):
        n = len(t)
        match = [0] * n
        c = 0
        for i in range(1, n):
            v = t[i]
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            match[i] = c
        return match

    def __init__(self, t):
        self.t = t
        self.max_match = self.build_max_match(t)

    def search(self, s):
        match = self.max_match
        t = self.t
        c = 0
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                return i - len(t) + 1
        return -1

    def find_all(self, s):
        match = self.max_match
        t = self.t
        c = 0
        pos = []
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                pos.append(i - len(t) + 1)
                c = match[c - 1]
        return pos


if __name__ == '__main__':
    pass
