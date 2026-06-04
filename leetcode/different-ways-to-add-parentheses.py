#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        items = []
        idx = 0
        while idx < len(input):
            s = input[idx]
            if s in string.digits:
                val = 0
                while idx < len(input) and input[idx] in string.digits:
                    val = val * 10 + ord(input[idx]) - ord('0')
                    idx += 1
                items.append(val)
            else:
                items.append(s)
                idx += 1

        if len(items) == 0:
            return []
        cache = {}

        def compute(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y

        def walk(s, e):
            if s == e:
                return [items[s]]
            elif (s + 2) == e:
                val = compute(items[s], items[e], items[s + 1])
                return [val]

            key = '{}-{}'.format(s, e)
            if key in cache:
                return cache[key]

            res = []
            for op_idx in range(s + 1, e, 2):
                outs1 = walk(s, op_idx - 1)
                outs2 = walk(op_idx + 1, e)
                for x in outs1:
                    for y in outs2:
                        res.append(compute(x, y, items[op_idx]))

            cache[key] = res
            return res

        res = walk(0, len(items) - 1)
        return res
