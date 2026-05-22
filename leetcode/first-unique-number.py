#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        from collections import Counter, deque
        self.cnt = Counter()
        self.st = deque()

        for x in nums:
            if self.cnt[x] >= 2:
                continue

            self.st.append(x)
            self.cnt[x] += 1

        self.balance()

    def balance(self):
        while self.st and self.cnt[self.st[0]] >= 2:
            self.st.popleft()

    def showFirstUnique(self) -> int:
        return self.st[0] if self.st else -1

    def add(self, value: int) -> None:
        if self.cnt[value] >= 2:
            return
        self.st.append(value)
        self.cnt[value] += 1
        self.balance()

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
