#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import base64
import gzip
import time
from hashlib import md5

from Crypto.Cipher import AES


def Decrypt(key: str, text: str) -> str:
    if len(key) < 32:
        key += ' ' * (32 - len(key))
    elif len(key) > 32:
        key = key[0:32]
    cipher = AES.new(bytes(key, encoding='utf-8'), AES.MODE_CBC, bytes(AES.block_size))
    ans = str(gzip.decompress(bytes.strip(cipher.decrypt(base64.b64decode(text)))), encoding='utf-8')
    return ans


def Pass(id, priv_key):
    prefix = str(id) + str(int(time.time()))
    pub_key = prefix + md5(bytes(prefix + priv_key, 'utf8')).hexdigest()
    print('恭喜通过第%d关,通关公钥:%s' % (id, pub_key))


# 41*x-31*x^2+74252906=0, wolfram alpha, x = -1547

def pow(a, b, MOD):
    ans = 1
    while b:
        if b % 2 == 1:
            ans *= a
            ans = ans % MOD
        a = (a * a) % MOD
        b = b // 2
    print(ans)
    return ans


# pow(1234567, 12345678901234567890, 999999997) # 42031180

def searchOperators():
    op = ['+', '-', '*', '/']
    for x in range(1 << 16):
        cnt = [0] * 4
        exp = ''
        for i in range(8):
            y = x & 0x3
            cnt[y] += 1
            exp += '%d' % (i + 1)
            exp += op[y]
            x = x >> 2
        exp += '9'
        ok = True
        for i in range(4):
            if cnt[i] == 0:
                ok = False
        if not ok:
            continue
        if eval(exp) == -497:
            print(exp)
            break


# searchOperators() # 1/2*3*4-5+6-7*8*9

# x^5-2*x^4+3*x^3-4*x^2-5*x-6=0, wolfram alpha, x ~= 2.19488
# 单调递增，二分计算。将x * 10 ^ 16, 最小值是0, 最大值是 3 * 10 ^ 16

def findRoot():
    scale = 10 ** 16

    def value(x):
        a = x ** 5
        b = 2 * (x ** 4) * (scale ** 1)
        c = 3 * (x ** 3) * (scale ** 2)
        d = 4 * (x ** 2) * (scale ** 3)
        e = 5 * x * (scale ** 4)
        f = 6 * (scale ** 5)
        return a - b + c - d - e - f

    s, e = 0, 3 * scale
    while s <= e:
        m = (s + e) // 2
        v = value(m)
        if v > 0:
            e = m - 1
        else:
            s = m + 1
    ans = str(e)
    ans = ans[-17] + '.' + ans[-16:-2]
    print(ans)


# findRoot() # 2.19488134060852


def mat_mul(x, y, MOD):
    sz = len(x)
    res = [[0] * sz for _ in range(sz)]
    for k in range(sz):
        for i in range(sz):
            for j in range(sz):
                res[i][j] = (res[i][j] + x[i][k] * y[k][j]) % MOD
    return res


def pow_mt(mt, n, MOD):
    ans = [[1, 0], [0, 1]]
    while n:
        if n % 2 == 1:
            ans = mat_mul(mt, ans, MOD)
        mt = mat_mul(mt, mt, MOD)
        n = n // 2
    return ans


def fix_vmcode():
    MOD = 99999999999999997
    ans = pow_mt([[3, 9], [7, 8]], (1 << 127) - 1, MOD)
    a, b = (ans[0][0] * 5 + ans[0][1] * 6) % MOD, (ans[1][0] * 5 + ans[1][1] * 6) % MOD
    key = str(a) + str(b)
    exec(Decrypt(key,
                 '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'))

# fix_vmcode()
