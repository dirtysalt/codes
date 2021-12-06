#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, Counter
        seg = defaultdict(list)
        sc, ec = Counter(), Counter()
        for i in range(len(pairs)):
            s, e = pairs[i]
            seg[pairs[i][0]].append(i)
            sc[s] += 1
            ec[e] += 1
        used = set()

        def find_path(node):
            path = []
            while True:
                ps = seg[node]
                while ps and ps[-1] in used:
                    ps.pop()
                if not ps:
                    break
                index = ps.pop()
                used.add(index)
                path.append(index)
                node = pairs[index][1]
            return path

        head = pairs[0][0]
        for x in sc.keys():
            if sc[x] > ec[x]:
                head = x
                break

        ans = find_path(head)

        while len(used) != len(pairs):
            for i in range(len(ans)):
                node = pairs[ans[i]][0]
                ext = find_path(node)
                if ext:
                    ans = ans[:i] + ext + ans[i:]
                    break
            # print(ans)
        return [pairs[x] for x in ans]


true, false, null = True, False, None
cases = [
    ([[5, 1], [4, 5], [11, 9], [9, 4]], [[11, 9], [9, 4], [4, 5], [5, 1]]),
    ([[1, 3], [3, 2], [2, 1]], [[1, 3], [3, 2], [2, 1]]),
    ([[1, 2], [1, 3], [2, 1]], [[1, 2], [2, 1], [1, 3]]),
    ([[17, 18], [18, 10], [10, 18]], [[17, 18], [18, 10], [10, 18]]),
    ([[5, 13], [10, 6], [11, 3], [15, 19], [16, 19], [1, 10], [19, 11], [4, 16], [19, 9], [5, 11], [5, 6], [13, 5],
      [13, 9], [9, 15], [11, 16], [6, 9], [9, 13], [3, 1], [16, 5], [6, 5]],
     [[4, 16], [16, 5], [5, 6], [6, 5], [5, 11], [11, 16], [16, 19], [19, 9], [9, 13], [13, 5], [5, 13], [13, 9],
      [9, 15], [15, 19], [19, 11], [11, 3], [3, 1], [1, 10], [10, 6], [6, 9]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().validArrangement, cases)

if __name__ == '__main__':
    pass
