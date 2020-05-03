#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import re
import re2


# note(yan): 非常不稳定，不要使用

class ReProxy:
    def __init__(self, pat, flags=0):
        self.m = re.compile(pat, flags)
        self.m2 = None
        if not flags and isinstance(pat, str):
            try:
                self.m2 = re2.compile(pat)
            except:
                print('re2 compile pat failed')
                pass

    def match(self, string, *args):
        if self.m2 and not args:
            return self.m2.match(string)
        return self.m.match(string)

    def search(self, string, *args):
        if self.m2 and not args:
            return self.m2.search(string)
        return self.m.search(string)

    def fullmatch(self, string, *args):
        if self.m2 and not args:
            return self.m2.fullmatch(string)
        return self.m.fullmatch(string)

    def sub(self, *args, **kwargs):
        return self.m.sub(*args, **kwargs)

    def subn(self, *args, **kwargs):
        return self.m.subn(*args, **kwargs)

    def find(self, *args, **kwargs):
        return self.m.find(*args, **kwargs)

    def findall(self, *args, **kwargs):
        return self.m.findall(*args, **kwargs)


def compile(pat, flags=0):
    return ReProxy(pat, flags)
