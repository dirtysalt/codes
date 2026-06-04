#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class FrequencyTracker:

    def __init__(self):
        from collections import Counter, defaultdict
        self.a = Counter()
        self.b = defaultdict(lambda: set())

    def add(self, number: int) -> None:
        old = self.a[number]
        self.a[number] += 1

        if number in self.b[old]:
            self.b[old].remove(number)
        self.b[old + 1].add(number)

    def deleteOne(self, number: int) -> None:
        old = self.a[number]
        if old == 0: return

        self.a[number] -= 1
        if number in self.b[old]:
            self.b[old].remove(number)
        if old != 1:
            self.b[old - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        ss = self.b[frequency]
        return len(ss) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

if __name__ == '__main__':
    pass
