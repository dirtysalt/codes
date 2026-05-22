#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def chr2int(c):
    return ord(c) - ord('a')


class Trie:
    def __init__(self):
        self.match = False
        self.nexts = [None] * 26

    def _op(self, s, op):
        root = self
        for c in s:
            ci = chr2int(c)
            if root.nexts[ci] is None:
                if op == 'insert':
                    node = Trie()
                    root.nexts[ci] = node
                else:
                    return False
            root = root.nexts[ci]
        if op == 'insert':
            root.match = True
        elif op == 'search':
            return root.match
        elif op == 'starts':
            return True

    def insert(self, s):
        self._op(s, 'insert')

    def search(self, s):
        return self._op(s, 'search')

    def startsWith(self, prefix):
        return self._op(prefix, 'starts')
