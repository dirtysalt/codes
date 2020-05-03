#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        visited = set()
        hp = []
        hp.append((nums1[0] + nums2[0], 0, 0))
        ans = []
        import heapq

        for _ in range(k):
            if not hp:
                break
            (x, i, j) = hp[0]
            # print(x, i, j)

            ans.append([nums1[i], nums2[j]])

            todo = []
            if (i + 1) < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                todo.append((i + 1, j))

            if (j + 1) < len(nums2) and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                todo.append((i, j + 1))

            if todo:
                # print('todo = {}'.format(todo))
                (i, j) = todo[0]
                heapq.heappushpop(hp, (nums1[i] + nums2[j], i, j))
                for (i, j) in todo[1:]:
                    heapq.heappush(hp, (nums1[i] + nums2[j], i, j))
            else:
                heapq.heappop(hp)

        return ans


cases = [
    ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
    ([1, 2], [3], 3, [[1, 3], [2, 3]]),
    ([1, 1, 2], [1, 2, 3], 10, [[1, 1], [1, 1], [2, 1], [1, 2], [1, 2], [2, 2], [1, 3], [1, 3], [2, 3]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kSmallestPairs, cases)
