#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min_st = []

    def push(self, x: int) -> None:
        self.st.append(x)
        if not self.min_st or self.min_st[-1] >= x:
            self.min_st.append(x)

    def pop(self) -> None:
        if not self.st:
            return
        x = self.st.pop()
        if self.min_st[-1] == x:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
