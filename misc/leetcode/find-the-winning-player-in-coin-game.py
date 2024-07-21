#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        n = min(x, y // 4)
        return "Alice" if n % 2 == 1 else "Bob"


if __name__ == '__main__':
    pass
