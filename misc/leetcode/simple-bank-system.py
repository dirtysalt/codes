#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.B = balance.copy()

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        a, b = account1 - 1, account2 - 1
        if a >= len(self.B): return False
        if b >= len(self.B): return False

        if self.B[a] >= money:
            self.B[a] -= money
            self.B[b] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        a = account - 1
        if a >= len(self.B): return False
        self.B[a] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        a = account - 1
        if a >= len(self.B): return False
        if self.B[a] >= money:
            self.B[a] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

if __name__ == '__main__':
    pass
