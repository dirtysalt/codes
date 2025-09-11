#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class RangeModule:

    def __init__(self):
        self.rs = []

    def find(self, start):
        s, e = 0, len(self.rs) - 1
        while s <= e:
            m = s + (e - s) // 2
            if self.rs[m][1] >= start:
                e = m - 1
            else:
                s = m + 1
        return s

    def find2(self, start):
        s, e = 0, len(self.rs) - 1
        while s <= e:
            m = s + (e - s) // 2
            if (self.rs[m][1] + 1) >= start:
                e = m - 1
            else:
                s = m + 1
        return s

    def print(self, *args):
        print(*args)
        pass

    def addRange(self, left: int, right: int) -> None:
        right -= 1
        self.print('A: {},{}, {}'.format(left, right, self.rs))
        idx = self.find2(left)
        if idx == len(self.rs):
            self.rs.append((left, right))
            self.print('ans: {}'.format(self.rs))
            return

        from_idx = idx
        s, e = self.rs[idx]
        assert (e + 1) >= left
        if (right + 1) < s:
            self.rs.insert(idx, (left, right))
            self.print('ans: {}'.format(self.rs))
            return

        s = min(s, left)
        e = max(e, right)
        idx += 1
        while idx < len(self.rs):
            if (e + 1) < self.rs[idx][0]:
                break
            e = max(e, self.rs[idx][1])
            idx += 1
        self.rs = self.rs[:from_idx] + [(s, e)] + self.rs[idx:]
        self.print('ans: {}'.format(self.rs))

    def queryRange(self, left: int, right: int) -> bool:
        right -= 1
        idx = self.find(left)
        if idx == len(self.rs):
            return False

        return self.rs[idx][0] <= left <= right <= self.rs[idx][1]

    def removeRange(self, left: int, right: int) -> None:
        right -= 1
        self.print('R: {},{}, {}'.format(left, right, self.rs))
        idx = self.find(left)
        if idx == len(self.rs):
            self.print('ans: {}'.format(self.rs))
            return

        from_idx = idx
        s, e = self.rs[idx]
        assert e >= left
        if s > right:
            self.print('ans: {}'.format(self.rs))
            return

        split = []
        if s < left:
            split.append((s, left - 1))
        if e > right:
            split.append((right + 1, e))

        idx += 1
        while idx < len(self.rs):
            if right < self.rs[idx][0]:
                break
            if right < self.rs[idx][1]:
                split.append((right + 1, self.rs[idx][1]))
                idx += 1
                break
            idx += 1
        self.rs = self.rs[:from_idx] + split + self.rs[idx:]
        self.print('ans: {}'.format(self.rs))


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

null, false, true = None, False, True

cases = [
    (["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"],
     [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]],
     [null, null, null, true, false, true]),
    (["RangeModule", "addRange", "addRange", "addRange", "queryRange", "queryRange", "queryRange", "removeRange",
      "queryRange"],
     [[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300], [600, 1000], [50, 150], [50, 100]],
     [null, null, null, null, true, false, false, null, false]),
    (["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange", "queryRange", "queryRange",
      "queryRange", "queryRange"],
     [[], [1, 10], [4, 6], [1, 5], [1, 6], [1, 7], [4, 5], [4, 6], [4, 7], [6, 7]],
     [null, null, null, false, false, false, false, false, false, true]),
    (["RangeModule", "addRange", "removeRange", "removeRange", "addRange", "removeRange", "addRange", "queryRange",
      "queryRange", "queryRange"],
     [[], [6, 8], [7, 8], [8, 9], [8, 9], [1, 3], [1, 8], [2, 4], [2, 9], [4, 6]],
     [null, null, null, null, null, null, null, true, true, true]),

    (["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange", "removeRange", "removeRange",
      "removeRange", "addRange", "addRange", "addRange", "removeRange", "addRange", "queryRange", "addRange",
      "addRange",
      "queryRange", "queryRange", "addRange", "removeRange", "removeRange", "removeRange", "queryRange", "queryRange",
      "addRange", "addRange", "queryRange", "addRange", "addRange", "removeRange", "addRange", "addRange", "queryRange",
      "removeRange", "queryRange", "removeRange", "addRange", "addRange", "queryRange", "removeRange", "removeRange",
      "addRange", "queryRange", "queryRange", "removeRange", "removeRange", "removeRange", "queryRange", "addRange",
      "removeRange", "removeRange", "queryRange", "removeRange", "removeRange", "queryRange", "addRange", "addRange",
      "removeRange", "queryRange", "queryRange", "addRange", "removeRange", "removeRange", "addRange", "addRange",
      "addRange", "addRange", "queryRange", "removeRange", "addRange", "addRange", "addRange", "queryRange", "addRange",
      "removeRange", "queryRange", "removeRange", "removeRange", "removeRange", "queryRange", "queryRange",
      "queryRange",
      "queryRange", "queryRange", "removeRange", "queryRange", "removeRange", "queryRange", "addRange", "queryRange"],
     [[], [14, 100], [1, 8], [77, 80], [8, 43], [4, 13], [3, 9], [45, 49], [41, 90], [58, 79], [4, 83], [34, 39],
      [84, 100],
      [8, 9], [32, 56], [35, 46], [9, 100], [85, 99], [23, 33], [10, 31], [15, 45], [52, 70], [26, 42], [30, 70],
      [60, 69],
      [10, 94], [2, 89], [26, 39], [46, 93], [30, 83], [42, 48], [47, 74], [39, 45], [14, 64], [3, 97], [16, 34],
      [28, 100],
      [19, 37], [27, 91], [55, 62], [64, 65], [2, 48], [55, 78], [21, 89], [31, 76], [13, 32], [2, 84], [21, 88],
      [12, 31],
      [89, 97], [56, 72], [16, 75], [18, 90], [46, 60], [20, 62], [28, 77], [5, 78], [58, 61], [38, 70], [24, 73],
      [72, 96],
      [5, 24], [43, 49], [2, 20], [4, 69], [18, 98], [26, 42], [14, 18], [46, 58], [16, 90], [32, 47], [19, 36],
      [26, 78],
      [7, 58], [42, 54], [42, 83], [3, 83], [54, 82], [71, 91], [22, 37], [38, 94], [20, 44], [37, 89], [15, 54],
      [1, 64],
      [63, 65], [55, 58], [23, 44], [25, 87], [38, 85], [27, 71]],
     [null, null, null, true, false, false, null, null, null, null, null, null, null, null, true, null, null, true,
      true,
      null, null, null, null, false, false, null, null, true, null, null, null, null, null, false, null, false, null,
      null,
      null, true, null, null, null, false, false, null, null, null, false, null, null, null, false, null, null, false,
      null,
      null, null, false, false, null, null, null, null, null, null, null, true, null, null, null, null, false, null,
      null,
      false, null, null, null, false, false, false, false, false, null, false, null, false, null, false]),

    (["RangeModule", "addRange", "addRange", "removeRange", "queryRange", "queryRange", "removeRange", "removeRange",
      "removeRange", "removeRange", "removeRange", "queryRange", "removeRange", "addRange", "removeRange", "addRange",
      "queryRange", "queryRange", "addRange", "addRange", "queryRange", "removeRange", "queryRange", "addRange",
      "queryRange", "removeRange", "removeRange", "addRange", "addRange", "removeRange", "removeRange", "removeRange",
      "addRange", "addRange", "queryRange", "queryRange", "queryRange", "queryRange", "queryRange", "removeRange",
      "removeRange", "queryRange", "addRange", "addRange", "addRange", "queryRange", "addRange", "addRange",
      "removeRange", "addRange", "queryRange", "removeRange", "addRange", "queryRange", "addRange", "addRange",
      "addRange", "queryRange", "addRange", "queryRange", "removeRange", "removeRange", "removeRange", "removeRange",
      "queryRange", "removeRange", "queryRange", "queryRange", "removeRange", "queryRange", "addRange", "addRange",
      "queryRange", "removeRange", "removeRange", "queryRange", "addRange", "removeRange", "removeRange", "addRange",
      "addRange", "addRange", "queryRange", "queryRange", "addRange", "queryRange", "removeRange", "queryRange",
      "removeRange", "addRange", "queryRange"],
     [[], [55, 62], [1, 29], [18, 49], [6, 98], [59, 71], [40, 45], [4, 58], [57, 69], [20, 30], [1, 40], [73, 93],
      [32, 93], [38, 100], [50, 64], [26, 72], [8, 74], [15, 53], [44, 85], [10, 71], [54, 70], [10, 45], [30, 66],
      [47, 98], [1, 7], [44, 78], [31, 49], [62, 63], [49, 88], [47, 72], [8, 50], [49, 79], [31, 47], [54, 87],
      [77, 78], [59, 100], [8, 9], [50, 51], [67, 93], [25, 86], [8, 92], [31, 87], [90, 95], [28, 56], [10, 42],
      [27, 34], [75, 81], [17, 63], [78, 90], [9, 18], [51, 74], [20, 54], [35, 72], [2, 29], [28, 41], [17, 95],
      [73, 75], [34, 43], [57, 96], [51, 72], [21, 67], [40, 73], [14, 26], [71, 86], [34, 41], [10, 25], [27, 68],
      [18, 32], [30, 31], [45, 61], [64, 66], [18, 93], [13, 21], [13, 46], [56, 99], [6, 93], [25, 36], [27, 88],
      [82, 83], [30, 71], [31, 73], [10, 41], [71, 72], [9, 56], [22, 76], [38, 74], [2, 77], [33, 61], [74, 75],
      [11, 43], [27, 75]],
     [null, null, null, null, false, false, null, null, null, null, null, false, null, null, null, null, false, false,
      null, null, true, null, false, null, false, null, null, null, null, null, null, null, null, null, true, true,
      false, false, true, null, null, false, null, null, null, true, null, null, null, null, false, null, null, false,
      null, null, null, true, null, true, null, null, null, null, false, null, false, false, null, false, null, null,
      false, null, null, false, null, null, null, null, null, null, true, true, null, true, null, false, null, null,
      false]
     )
]

import aatest_helper

aatest_helper.run_simulation_cases(RangeModule, cases)
