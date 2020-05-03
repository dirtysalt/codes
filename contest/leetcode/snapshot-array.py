#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        from collections import defaultdict
        self.array = defaultdict(int)
        self.snap_id = 0
        self.index_vsn = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        snap_id = self.snap_id
        key = '{}.{}'.format(index, snap_id)
        self.array[key] = val
        vsn = self.index_vsn[index]
        if vsn and vsn[-1] == snap_id:
            pass
        else:
            vsn.append(snap_id)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        vsn = self.index_vsn[index]
        if not vsn:
            return 0
        # 这个二分法特别容易出错，还需要考虑没有比snap_id小的情况
        import bisect
        idx = bisect.bisect(vsn, snap_id)
        # print(vsn, snap_id, idx)
        if idx == 0:
            return 0
        assert vsn[idx-1] <= snap_id
        snap_id = vsn[idx-1]
        key = '{}.{}'.format(index, snap_id)
        return self.array[key]


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
