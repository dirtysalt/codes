#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ss = date.split('-')
        res = []
        for s in ss:
            res.append(str(bin(int(s)))[2:])
        return '-'.join(res)


if __name__ == '__main__':
    pass
