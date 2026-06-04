#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ans = [0] * numberOfUsers

        seq = []
        for msg, ts, data in events:
            ts = int(ts)
            if msg == 'MESSAGE':
                seq.append((ts, 1, data))
            elif msg == 'OFFLINE':
                data = int(data)
                seq.append((ts, 0, data))
                seq.append((ts + 60, -1, data))

        seq.sort(key=lambda x: (x[0], x[1]))
        online = set(range(numberOfUsers))
        for ts, msg, data in seq:
            if msg == -1:
                online.add(data)
            elif msg == 0:
                online.remove(data)
            elif data == 'ALL':
                for i in range(len(ans)):
                    ans[i] += 1
            elif data == 'HERE':
                for x in online:
                    ans[x] += 1
            else:
                for i in [int(x[2:]) for x in data.split()]:
                    ans[i] += 1
        return ans


if __name__ == '__main__':
    pass
