#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class ATM:

    def __init__(self):
        self.count = [0, 0, 0, 0, 0]
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for i in reversed(range(5)):
            x = min(self.count[i], amount // self.values[i])
            ans[i] = x
            amount -= x * self.values[i]
        if amount != 0:
            return [-1]
        for i in range(5):
            self.count[i] -= ans[i]
        return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)

if __name__ == '__main__':
    pass
