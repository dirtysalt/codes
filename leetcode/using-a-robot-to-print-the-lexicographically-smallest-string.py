#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        s = [ord(x) - ord('a') for x in s]
        tail = [[] for _ in range(26)]
        for i in reversed(range(n)):
            tail[s[i]].append(i)

        st = [26]

        def find_next(now):
            last = st[-1]
            for j in range(last):
                while tail[j] and tail[j][-1] < now:
                    tail[j].pop()
                if tail[j]:
                    dest = tail[j][-1]
                    st.extend(s[now: dest + 1])
                    return dest + 1
            return None

        consume = 0
        ans = []
        while consume < n:
            off = find_next(consume)
            if off is None:
                ans.append(st.pop())
            else:
                consume = off

        while st:
            ans.append(st.pop())
        # remove 26
        ans.pop()
        ans = ''.join([chr(x + ord('a')) for x in ans])
        return ans


true, false, null = True, False, None
cases = [
    ("zza", "azz"),
    ("bac", "abc"),
    ("bdda", "addb"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().robotWithString, cases)

if __name__ == '__main__':
    pass
