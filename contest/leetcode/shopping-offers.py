#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def search(sidx, needs):
            if sidx == len(special):
                res = 0
                for idx in range(len(price)):
                    res += price[idx] * needs[idx]
                return res

            res = search(sidx + 1, needs)

            reqs = special[sidx][:-1]
            cost = special[sidx][-1]
            k = 0
            while True:
                ok = True
                k += 1
                for req_idx in range(len(reqs)):
                    if needs[req_idx] < reqs[req_idx] * k:
                        ok = False
                        break
                if not ok:
                    break

                for req_idx in range(len(reqs)):
                    needs[req_idx] -= reqs[req_idx] * k

                tmp = search(sidx + 1, needs)
                res = min(res, tmp + cost * k)

                for req_idx in range(len(reqs)):
                    needs[req_idx] += reqs[req_idx] * k
            return res

        return search(0, needs)
