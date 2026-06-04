#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        names = {}
        for r in recipes:
            if r not in names:
                p = len(names)
                names[r] = p
        for xs in ingredients:
            for x in xs:
                if x not in names:
                    p = len(names)
                    names[x] = p

        # print(names)

        n = len(names)
        adj = [[] for _ in range(n)]
        wait = [0] * n
        for i in range(len(recipes)):
            r = recipes[i]
            p = names[r]
            wait[p] = len(ingredients[i])

            for x in ingredients[i]:
                p2 = names[x]
                adj[p2].append(p)

        queue = []
        for x in supplies:
            if x not in names: continue
            p = names[x]
            for p2 in adj[p]:
                wait[p2] -= 1
                if wait[p2] == 0:
                    queue.append(p2)

        while queue:
            p = queue.pop()
            for p2 in adj[p]:
                wait[p2] -= 1
                if wait[p2] == 0:
                    queue.append(p2)

        ans = []
        for r in recipes:
            p = names[r]
            if wait[p] <= 0:
                ans.append(r)
        return ans


if __name__ == '__main__':
    pass
