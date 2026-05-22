#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class ARC4:
    def __init__(self):
        self.st = [0] * 256
        self.indx = 0
        self.jndx = 0

    def reset(self):
        self.indx = 0
        self.jndx = 0
        for i in range(256):
            self.st[i] = i

    def key(self, bs):
        self.indx = 0
        offset, n = 0, len(bs)
        k = 0
        while n > 0:
            for i in range(256):
                k += self.st[i]
                k += int(bs[offset + (i % n)])
                k %= 256
                self.st[i], self.st[k] = self.st[k], self.st[i]
            offset += 256
            n -= 256

    def crypt(self, bs):
        n = len(bs)
        res = []
        for i in range(n):
            self.indx = (self.indx + 1) % 256
            self.jndx += self.st[self.indx]
            self.jndx %= 256
            indx, jndx = self.indx, self.jndx
            self.st[indx], self.st[jndx] = self.st[jndx], self.st[indx]
            tmp = (self.st[indx] + self.st[jndx]) % 256
            b = bs[i] ^ self.st[tmp]
            res.append(b)
        return bytes(res)


arc4 = ARC4()
arc4.reset()
arc4.key(b'hello')
a = arc4.crypt(b'world')
b = arc4.crypt(b'hello')
print(a, b)

arc4.reset()
arc4.key(b'hello')
c = arc4.crypt(a)
d = arc4.crypt(b)
print(c, d)

arc4.reset()
arc4.key(b'hello2')
c = arc4.crypt(a)
d = arc4.crypt(b)
print(c, d)
