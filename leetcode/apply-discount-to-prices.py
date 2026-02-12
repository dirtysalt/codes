#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        xs = sentence.split()
        xs2 = []
        r = (1 - discount / 100)
        for x in xs:
            if x[0] == '$' and x[1:].isdigit():
                v = float(x[1:]) * r
                xs2.append('$%.2f' % v)
            else:
                xs2.append(x)
        ans = ' '.join(xs2)
        return ans


if __name__ == '__main__':
    pass
