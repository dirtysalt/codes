#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

# note(yan): 这题目坑太多了，有好几处地方想优化但是都没有考虑到错误情况
# 1. 放入tx的时候想快速做去重
# 2. 想线性扫描做优化


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        from collections import defaultdict
        people_tx = defaultdict(list)
        for tx_id, tx in enumerate(transactions):
            (name, time, amount, city) = tx.split(',')
            time, amount = int(time), int(amount)
            people_tx[name].append((time, amount, city, tx_id))

        ans = []

        for name, txs in people_tx.items():
            txs.sort(key=lambda x: x[0])
            print(name, txs)
            for idx, tx in enumerate(txs):
                if tx[1] > 1000:
                    ans.append(tx)

                for tx2 in txs[idx+1:]:
                    if (tx2[0] - tx[0]) > 60:
                        break
                    if tx2[2] != tx[2]:
                        ans.append(tx)
                        ans.append(tx2)

        ans.sort(key=lambda x: x[3])
        dup = set()
        res = []
        for tx in ans:
            tx_id = tx[3]
            if tx_id in dup:
                continue
            dup.add(tx_id)
            res.append(transactions[tx_id])
        return res


import aatest_helper

cases = [
    (["alice,20,800,mtv", "alice,50,100,beijing"],
     ["alice,20,800,mtv", "alice,50,100,beijing"]),
    (["alice,20,800,mtv", "bob,50,1200,mtv"], ["bob,50,1200,mtv"]),
    (["alice,20,800,mtv", "alice,50,1200,mtv"], ["alice,50,1200,mtv"]),
    (["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona", "bob,820,596,bangkok", "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"],
     ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"]),
    (["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona", "alex,587,402,bangkok", "chalicefy,973,830,barcelona", "alex,932,86,bangkok", "bob,188,989,amsterdam"],
     ["bob,627,1973,amsterdam", "alex,387,885,bangkok", "alex,355,1029,barcelona"]),

]

aatest_helper.run_test_cases(Solution().invalidTransactions, cases)
