#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from __future__ import (absolute_import, division, print_function, unicode_literals)

import random
def miller_rabin(n, k=10):
	if n == 2 or n == 3:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

def makeprimes(n):
    p = [0] * (n + 1)
    sz = len(p)
    for i in range(2, sz):
        if i * i >= sz: break
        if p[i] == 1: continue
        for j in range(i, sz):
            if i * j >= sz: break
            p[i*j]=1
    p = [bool(1-x) for x in p]
    return p

def test():
    n = 10000
    passed = True
    primes = makeprimes(n)
    for x in range(2, n+1):
        a = primes[x]
        b = miller_rabin(x, k = 30)
        if a != b:
            print('x = {}, p = {}, mb = {}'.format(x, a, b))
            passed = False
    if passed:
        print('all cases passed')

if __name__ == '__main__':
    test()
