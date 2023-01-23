#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sortedcontainers import SortedList


class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.sl = SortedList()
        self.sl.add((0, n))
        from collections import defaultdict
        self.idList = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        n = self.n
        sl = self.sl
        res = None
        for off, cap in self.sl:
            if cap >= size:
                res = (off, size)
                self.sl.remove((off, cap))
                if cap - size > 0:
                    self.sl.add((off + size, cap - size))
                break
        if res is not None:
            self.idList[mID].append(res)
            return res[0]
        return -1

    def free(self, mID: int) -> int:
        ss = self.idList[mID]
        self.idList[mID] = []
        ans = 0
        for s in ss:
            ans += s[1]
            self.sl.add(s)
        self.compact()
        return ans

    def compact(self):
        area = []
        last = None
        for off, cap in self.sl:
            if last is None:
                last = (off, cap)
            elif last[0] + last[1] == off:
                last = (last[0], last[1] + cap)
            else:
                area.append(last)
                last = (off, cap)
        if last:
            area.append(last)
        self.sl = SortedList(area)

    # Your Allocator object will be instantiated and called as such:


# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
true, false, null = True, False, None
import aatest_helper

cases = [
    (["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate",
      "free"],
     [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]],
     [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]),
    (["Allocator", "allocate", "allocate", "allocate", "allocate", "free", "free", "free", "allocate", "allocate",
      "allocate", "allocate", "free", "free", "free", "free", "free", "free", "free", "allocate", "free", "free",
      "allocate", "free", "allocate", "allocate", "free", "free", "free", "allocate", "allocate", "allocate",
      "allocate", "free", "allocate", "free", "free", "allocate", "allocate", "allocate", "allocate", "allocate",
      "allocate", "allocate", "free", "free", "free", "free"],
     [[50], [12, 6], [28, 16], [17, 23], [50, 23], [6], [10], [10], [16, 8], [17, 41], [44, 27], [12, 45], [33], [8],
      [16], [23], [23], [23], [29], [38, 32], [29], [6], [40, 11], [16], [22, 33], [27, 5], [3], [10], [29], [16, 14],
      [46, 47], [48, 9], [36, 17], [33], [14, 24], [16], [8], [2, 50], [31, 36], [17, 45], [46, 31], [2, 6], [16, 2],
      [39, 30], [33], [45], [30], [27]],
     [null, 0, 12, -1, -1, 12, 0, 0, -1, -1, -1, 0, 0, 0, 28, 0, 0, 0, 0, 12, 0, 0, -1, 0, -1, -1, 0, 0, 0, -1, -1, -1,
      -1, 0, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, 0, 12, 0, 0]),
]

aatest_helper.run_simulation_cases(Allocator, cases)

if __name__ == '__main__':
    pass
