#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def tosec(s):
            ss = s.split(':')
            m = int(ss[0])
            sec = int(ss[1])
            return m * 60 + sec

        a = [tosec(x) for x in event1]
        b = [tosec(x) for x in event2]

        if b[0] <= a[1] and b[1] >= a[0]:
            return True
        if a[0] <= b[1] and a[1] >= b[0]:
            return True

        return False


if __name__ == '__main__':
    pass
