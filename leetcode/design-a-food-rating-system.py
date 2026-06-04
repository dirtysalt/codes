#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        from sortedcontainers import SortedList
        from collections import defaultdict
        self.dd = defaultdict(SortedList)
        self.r = {}
        self.c = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.dd[c].add(((-r, f)))
            self.r[f] = r
            self.c[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.c[food]
        r = self.r[food]
        self.r[food] = newRating
        sl = self.dd[c]

        sl.remove((-r, food))
        sl.add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        sl = self.dd[cuisine]
        return sl[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
if __name__ == '__main__':
    pass
