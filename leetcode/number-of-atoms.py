#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


class Solution:
    """
    @param formula: a string
    @return: return a string
    """

    def countOfAtoms(self, formula):
        # write your code here

        def isdigit(s):
            return s in '0123456789'

        def multiply(res, mul):
            for k in res:
                res[k] *= mul

        def merge(res, delta):
            for k in delta:
                if k not in res:
                    res[k] = 0
                res[k] += delta[k]

        def parse_bracket(s, idx):
            assert s[idx] == '('
            idx += 1
            res, idx = parse(s, idx)
            assert s[idx] == ')'
            idx += 1
            if idx < len(s) and isdigit(s[idx]):
                val, idx = parse_digit(s, idx)
                multiply(res, val)
            return res, idx

        def parse_digit(s, idx):
            val = 0
            while idx < len(s) and isdigit(s[idx]):
                val = val * 10 + (ord(s[idx]) - ord('0'))
                idx += 1
            return val, idx

        def parse_item(s, idx):
            ele = s[idx]
            idx += 1
            assert ele in string.ascii_uppercase
            while idx < len(s) and (s[idx] in string.ascii_lowercase):
                ele += s[idx]
                idx += 1
            res = {ele: 1}
            if idx < len(s) and isdigit(s[idx]):
                val, idx = parse_digit(s, idx)
                multiply(res, val)
            return res, idx

        def parse(s, idx):
            res = {}
            while idx < len(s):
                if s[idx] == '(':
                    delta, idx = parse_bracket(s, idx)
                    merge(res, delta)
                elif s[idx] == ')':
                    break
                else:
                    delta, idx = parse_item(s, idx)
                    merge(res, delta)
            return res, idx

        counter, _ = parse(formula, 0)
        cs = list(counter.keys())
        cs.sort()
        res = ''
        for c in cs:
            cnt = counter[c]
            res += c
            if cnt != 1:
                res += '{}'.format(cnt)
        return res
