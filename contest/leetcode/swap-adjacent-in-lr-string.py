#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """

        if len(start) != len(end):
            return False
        start = list(start)
        end = list(end)
        n = len(start)
        p = 0
        while p < n:
            if start[p] == end[p]:
                p += 1
                continue

            if start[p] == 'R' and end[p] == 'X':
                # scan to next 'X'
                p2 = p + 1
                while p2 < n and start[p2] == 'R':
                    p2 += 1

                if p2 < n and start[p2] == 'X':
                    start[p], start[p2] = start[p2], start[p]
                else:
                    return False

                p += 1
                continue

            if start[p] == 'X' and end[p] == 'L':
                # scan to next 'L':
                p2 = p + 1
                while p2 < n and start[p2] == 'X':
                    p2 += 1
                if p2 < n and start[p2] == 'L':
                    start[p], start[p2] = start[p2], start[p]
                else:
                    return False

                p += 1
                continue

            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print((sol.canTransform("XXXXXLXXXX", "LXXXXXXXXX")))
