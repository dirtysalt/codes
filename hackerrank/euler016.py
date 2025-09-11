#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 10 ** 4
table = [0] * (N + 1)
table[0] = 1
prod = [1]
for i in range(1, N + 1):
    carry = 0
    for idx in range(len(prod)):
        prod[idx] *= 2
    for idx in range(len(prod)):
        prod[idx] += carry
        carry = prod[idx] // 10
        prod[idx] %= 10
    while carry:
        prod.append(carry % 10)
        carry //= 10
    # print('2 ** {} = {}'.format(i, ''.join(map(str, prod[::-1]))))
    res = sum(prod)
    table[i] = res

# print('OK')
t = int(input())
for _ in range(t):
    n = int(input())
    print((table[n]))
