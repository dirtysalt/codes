#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class RangeModule:
    def __init__(self):
        self.rs = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        rs = []
        a, b = left, right
        pushed = False
        for (x, y) in self.rs:
            if y < a or x > b:
                if x > b and not pushed:
                    rs.append((a, b))
                    pushed = True
                rs.append((x, y))
            else:
                a, b = min(a, x), max(b, y)
        if not pushed:
            rs.append((a, b))
        # rs.sort(key=lambda x: x[1])
        self.rs = rs

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        s, e = 0, len(self.rs) - 1
        while s <= e:
            m = (s + e) // 2
            if self.rs[m][1] < right:
                s = m + 1
            else:
                e = m - 1
        if s < len(self.rs) and self.rs[s][0] <= left and self.rs[s][1] >= right:
            return True
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        rs = []
        for (x, y) in self.rs:
            if y < left or x > right:
                rs.append((x, y))
                continue
            if x < left:
                rs.append((x, left))
            if y > right:
                rs.append((right, y))
        # rs.sort(key=lambda x: x[1])
        self.rs = rs


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

if __name__ == '__main__':
    rm = RangeModule()
    rm.addRange(10, 20)
    # rm.addRange(20, 22)
    # rm.addRange(24, 26)
    # rm.addRange(22, 24)
    rm.removeRange(14, 16)
    print(rm.rs)
    print(rm.queryRange(10, 14))
    print(rm.queryRange(13, 15))
    print(rm.queryRange(16, 17))
