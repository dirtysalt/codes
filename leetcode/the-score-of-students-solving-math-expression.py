#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:

        def eval_correct(s):
            i = 0
            st = []
            while i < len(s):
                if s[i] == '*':
                    x = st[-1]
                    st.pop()
                    st.append(x * int(s[i + 1]))
                    i += 1
                elif s[i] != '+':
                    st.append(int(s[i]))
                i += 1

            return sum(st)

        import functools

        @functools.lru_cache(maxsize=None)
        def find_all(s):
            if len(s) == 1:
                return set([int(s[0])])

            res = set()
            for i in range(1, len(s), 2):
                a = find_all(s[:i])
                b = find_all(s[i + 1:])
                if s[i] == '+':
                    res.update([x + y for x in a for y in b])
                else:
                    res.update([x * y for x in a for y in b])

            return {x for x in res if x <= 1000}

            return res

        ok = eval_correct(s)
        combs = find_all(s)
        # print(combs)
        ans = 0
        for x in answers:
            if x == ok:
                ans += 5
            elif x in combs:
                ans += 2

        return ans


true, false, null = True, False, None
cases = [
    ("7+3*1*2", [20, 13, 42], 7),
    ("3+5*2", [13, 0, 10, 13, 13, 16, 16], 19),
    ("6+0*1", [12, 9, 6, 4, 8, 6], 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().scoreOfStudents, cases)

if __name__ == '__main__':
    pass
