#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class LUPrefix:

    def __init__(self, n: int):
        self.mask = [0] * (n + 2)
        self.last = 0
        self.n = n

    def upload(self, video: int) -> None:
        self.mask[video] = 1

    def longest(self) -> int:
        while self.mask[self.last + 1]:
            self.last += 1
        return self.last


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

if __name__ == '__main__':
    pass
