#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(people)
        if n == 0: return []
        counter = [0] * n

        for i in range(n):
            counter[i] = people[i][1]

        res = []
        while len(res) < n:
            min_idx = None
            for x in range(n):
                if counter[x] == 0:
                    if min_idx is None or people[x][0] < people[min_idx][0]:
                        min_idx = x

            res.append(min_idx)
            counter[min_idx] -= 1

            for x in range(n):
                if counter[x] > 0 and people[x][0] <= people[min_idx][0]:
                    counter[x] -= 1

        res = [people[x] for x in res]
        return res


if __name__ == '__main__':
    sol = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(sol.reconstructQueue(people))
