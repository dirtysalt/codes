#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Trie:
    def __init__(self):
        self.pfx = set()
        self.match = set()

    def insert(self, s):
        for i in range(1, len(s) + 1):
            w = s[:i]
            self.pfx.add(w)
        self.match.add(s)

    def search(self, s):
        return s in self.match

    def startsWith(self, prefix):
        return prefix in self.pfx
