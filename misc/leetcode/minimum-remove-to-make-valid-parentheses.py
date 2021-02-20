#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        removed = set()
        for idx, c in enumerate(s):
            if c == '(':
                st.append(idx)
            elif c == ')':
                if not st:
                    removed.add(idx)
                    continue
                st.pop()
            else:
                pass
        while st:
            x = st.pop()
            removed.add(x)

        ans = [c for (idx, c) in enumerate(s) if idx not in removed]
        ans = ''.join(ans)
        return ans


cases = [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", "")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minRemoveToMakeValid, cases)
