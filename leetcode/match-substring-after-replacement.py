#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        from collections import defaultdict
        m = defaultdict(set)
        for x, y in mappings:
            m[x].add(y)
        for offset in range(len(s) - len(sub) + 1):
            ok = True
            for i in range(len(sub)):
                a = s[i + offset]
                b = sub[i]
                if a == b: continue
                if a in m[b]:
                    continue
                ok = False
                break
            if ok: return True
        return False


true, false, null = True, False, None
cases = [
    ("fool3e7bar", "leet", [["e", "3"], ["t", "7"], ["t", "8"]], true),
    ("fooleetbar", "f00l", [["o", "0"]], false),
    ("Fool33tbaR", "leetd", [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]], true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().matchReplacement, cases)

if __name__ == '__main__':
    pass
