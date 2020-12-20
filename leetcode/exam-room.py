#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class ExamRoom:
    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = set()
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        # print('seats = {}'.format(self.seats))
        size = len(self.seats)
        res = 0
        if size == 0:
            self.seats.add(res)
            return res

        s = -1
        seats = list(self.seats)
        seats.sort()
        seats.append(self.N)

        # two sides are exceptions.
        max_interval = 0
        max_result = None
        for k in seats:
            if s == -1:
                m = 0
                interval = k - m
            elif k == self.N:
                m = self.N - 1
                interval = m - s
            else:
                m = (k + s) // 2
                interval = min(m - s, k - m)

            if interval > max_interval:
                max_interval = interval
                max_result = m
            s = k

        # print(max_interval, max_result)
        res = max_result
        self.seats.add(res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.seats.remove(p)


if __name__ == '__main__':
    actions = ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat",
               "seat",
               "seat", "seat", "leave", "leave", "seat", "seat", "leave", "seat", "leave", "seat", "leave", "seat",
               "leave",
               "seat", "leave", "leave", "seat", "seat", "leave", "leave", "seat", "seat", "leave"]
    values = [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0], [4], [], [], [7], [], [3], [], [3],
              [], [9],
              [], [0], [8], [], [], [0], [8], [], [], [2]]

    actions = ["ExamRoom", "seat", "seat", "seat", "leave", "seat", "leave", "seat", "leave", "seat", "leave"]
    values = [[3], [], [], [], [2], [], [2], [], [1], [], [0]]

    sol = None
    for (act, val) in zip(actions, values):
        if act == 'ExamRoom':
            sol = ExamRoom(val[0])
        elif act == 'seat':
            print((sol.seat()))
        else:
            sol.leave(val[0])
