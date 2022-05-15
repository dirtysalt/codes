#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.sl = SortedList()
        self.result = 0

    def add(self, left: int, right: int) -> None:
        sl = self.sl
        right += 1

        r = (left, right)
        sl.add(r)
        idx = sl.index(r)
        n = len(sl)

        # print(sl, r, idx)

        d = []

        begin = left
        end = right

        # search before.
        i = idx - 1
        while i >= 0 and sl[i][1] >= begin:
            begin = sl[i][0]
            end = max(end, sl[i][1])
            d.append(sl[i])
            i -= 1

        i = idx + 1
        while i < n and sl[i][0] <= end:
            end = max(end, sl[i][1])
            d.append(sl[i])
            i += 1

        self.result += (right - left)

        if len(d) == 0:
            # print(self.result)
            return

        self.result += (end - begin)
        d.append((left, right))
        for r in d:
            # print('remove', r)
            self.result -= (r[1] - r[0])
            sl.remove(r)
        # print('add', (begin, end))
        sl.add((begin, end))
        # print(self.result)

    def count(self) -> int:
        return self.result

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()


if __name__ == '__main__':
    pass
