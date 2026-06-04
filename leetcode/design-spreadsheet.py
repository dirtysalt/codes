#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Spreadsheet:

    def __init__(self, rows: int):
        from collections import defaultdict
        self.v = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.v[cell] = value

    def resetCell(self, cell: str) -> None:
        self.v[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        if x[0].isdigit():
            x = int(x)
        else:
            x = self.v[x]
        if y[0].isdigit():
            y = int(y)
        else:
            y = self.v[y]
        return x + y


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

if __name__ == '__main__':
    pass
