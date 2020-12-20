#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        from collections import Counter
        seen = set()
        cc = Counter(text)
        st = []

        for c in text:
            if c in seen:
                cc[c] -= 1
                continue

            while st:
                t = st[-1]
                if cc[t] > 0 and t > c:
                    st.pop()
                    seen.remove(t)
                else:
                    break

            st.append(c)
            cc[c] -= 1
            seen.add(c)

        ans = ''.join(st)
        return ans
