# codes

python code to compute fibonacci number

```python
#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def MatMul(a, b, MOD):
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD
    return res


def PowMat(mt, k, MOD):
    n = len(mt)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1

    while k:
        if k % 2 == 1:
            res = MatMul(res, mt, MOD)
        mt = MatMul(mt, mt, MOD)
        k = k // 2
    return res

def FibMat(n, MOD):
    mt = [[1,1],[1,0]]
    tmp = PowMat(mt, n, MOD)
    f1, f0 = 1, 0
    fn = (tmp[1][0] * f1 + tmp[1][1] * f0) % MOD
    return fn

def FibIter(n, MOD):
    a, b = 1, 0
    for i in range(n):
        a, b = a + b, a
        a, b = a % MOD, b % MOD
    return b

n = 1 << 24
MOD = 10 ** 9 + 7
print(FibMat(n, MOD))
print(FibIter(n, MOD))

```
