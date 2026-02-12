#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        pf = set(positive_feedback)
        nf = set(negative_feedback)
        Result = []
        for sid, r in zip(student_id, report):
            ss = r.split()
            res = 0
            for s in ss:
                if s in pf:
                    res += 3
                if s in nf:
                    res -= 1
            Result.append((sid, res))

        Result.sort(key=lambda x: (-x[1], x[0]))
        ans = [x[0] for x in Result[:k]]
        return ans


if __name__ == '__main__':
    pass
