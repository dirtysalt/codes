#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import json


def solve(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        ans = 0
        for x in data:
            ans += solve(x)
        return ans
    if isinstance(data, dict):
        ans = 0
        for k, v in data.items():
            ans += solve(v)
        return ans

    if isinstance(data, str):
        return 0
    print(data)
    return 0


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    with open(input_file) as fh:
        data = json.load(fh)
    ans = solve(data)
    print(ans)


if __name__ == '__main__':
    main()
