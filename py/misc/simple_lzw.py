#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class CompressState:
    def __init__(self):
        self.table = {}
        self.offset = 0
        self.reset()

    def reset(self):
        self.offset = 0
        for i in range(256):
            bs = bytes([i])
            self.table[bs] = self.offset
            self.offset += 1

    def print(self):
        print('===== compress state =====')
        for k, v in self.table.items():
            if v >= 256:
                print('{} => {}'.format(v, k))

    def lookup(self, bs):
        # print('lookup bs = {}'.format(bs))
        return self.table.get(bs)

    def insert(self, bs):
        # print('insert bs = {}'.format(bs))
        self.table[bs] = self.offset
        self.offset += 1

    def compress(self, bs):
        p = 0
        res = []
        c = None

        i = 0
        while i < len(bs):
            clip = bs[p:i + 1]
            x = self.lookup(clip)
            if x is None:
                self.insert(clip)
                assert c is not None
                res.append(c)
                p = i
            else:
                c = x
                i = i + 1

        assert c is not None
        res.append(c)
        return res


class DecompressState:
    def __init__(self):
        self.table = []
        self.reset()

    def reset(self):
        for i in range(256):
            bs = bytes([i])
            self.table.append(bs)

    def lookup(self, code):
        if code < len(self.table):
            return self.table[code]
        return None

    def insert(self, bs):
        self.table.append(bs)

    def decompress(self, codes):
        res = bytes([])

        old = self.lookup(codes[0])
        res += old

        i = 1
        while i < len(codes):
            c = codes[i]
            s = self.lookup(c)
            if s is None:
                s = old + old[:1]
            res += s
            self.insert(old + s[:1])
            old = s
            i = i + 1

        return res


def test():
    text = "hello, world\0\0\0"
    # text = 'BABAABAAA'
    st = CompressState()
    st2 = DecompressState()

    for i in range(20):
        print('===== run =====')
        bs = text.encode('utf8')
        res = st.compress(bs)
        # st.print()
        print(' '.join(['%d' % x for x in res]))

        bs2 = st2.decompress(res)
        text2 = bs2.decode('utf8')
        print(text2)


test()
