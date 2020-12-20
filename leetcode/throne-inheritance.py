#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import defaultdict

from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def build(self):
        ans = []

        def visit(x):
            if x not in self.deaths:
                ans.append(x)
            for c in self.children[x]:
                visit(c)

        visit(self.king)
        return ans

    def getInheritanceOrder(self) -> List[str]:
        return self.build()

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
