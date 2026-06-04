#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ss = title.split()
        ss = [s.capitalize() if len(s) > 2 else s.lower() for s in ss]
        return ' '.join(ss)


if __name__ == '__main__':
    pass
