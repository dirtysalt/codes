#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countCollisions(self, directions: str) -> int:
        st = []
        ans = 0

        for c in directions:
            while st:
                if st[-1] == c or st[-1] == 'L':
                    break

                if st[-1] == 'R':
                    st.pop()
                    if c == 'L':
                        ans += 2
                    elif c == 'S':
                        ans += 1
                    c = 'S'
                elif st[-1] == 'S':
                    if c == 'L':
                        st.pop()
                        ans += 1
                        c = 'S'
                    else:
                        assert c == 'R'
                        break
            st.append(c)
        # print(st)
        return ans


true, false, null = True, False, None
cases = [
    ("RLRSLL", 5),
    ("LLRR", 0),
    ("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR", 20)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countCollisions, cases)

if __name__ == '__main__':
    pass
