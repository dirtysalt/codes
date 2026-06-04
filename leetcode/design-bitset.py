#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Bitset:

    def __init__(self, size: int):
        self.c = 1
        self.bits = [0] * size
        self.ones = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if self.bits[idx] != self.c:
            self.bits[idx] = self.c
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] == self.c:
            self.bits[idx] = 1 - self.c
            self.ones -= 1

    def flip(self) -> None:
        self.c = 1 - self.c
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        ans = []
        if self.c == 1:
            ans.extend([str(x) for x in self.bits])
        else:
            ans.extend([str(1 - x) for x in self.bits])
        return ''.join(ans)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

if __name__ == '__main__':
    pass
