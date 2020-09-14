#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class SnapshotArray:

    def __init__(self, length: int):
        from collections import defaultdict
        self.data = defaultdict(list)
        self.version = 0

    def set(self, index: int, val: int) -> None:
        version = self.version
        xs = self.data[index]
        if xs and xs[-1][0] == version:
            xs[-1] = (version, val)
        else:
            xs.append((version, val))

    def snap(self) -> int:
        self.version += 1
        return self.version - 1

    def get(self, index: int, snap_id: int) -> int:
        xs = self.data[index]
        s, e = 0, len(xs) - 1
        while s <= e:
            m = (s + e) // 2
            if xs[m][0] > snap_id:
                e = m - 1
            else:
                s = m + 1

        if 0 <= e < len(xs):
            v = xs[e]
            assert (v[0] <= snap_id)
            return v[1]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

null = None

cases = [
    (["SnapshotArray", "set", "snap", "set", "get"], [
        [3], [0, 5], [], [0, 6], [0, 0]], [null, null, 0, null, 5]),
    (["SnapshotArray", "set", "snap", "set", "get"],
     [[3], [0, 5], [], [0, 6], [0, 0]], [null, null, 0, null, 5]),
]

import aatest_helper

aatest_helper.run_simulation_cases(SnapshotArray, cases)
