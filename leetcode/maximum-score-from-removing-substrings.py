#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pat = ('ab', 'ba')
        val = (x, y)
        if x < y:
            pat = ('ba', 'ab')
            val = (y, x)

        def clear(st):
            st2 = []
            res = 0
            for c in st:
                st2.append(c)
                if ''.join(st2[-2:]) == pat[1]:
                    res += val[1]
                    st2.pop()
                    st2.pop()
            st.clear()
            return res

        ans = 0
        st = []
        for i in range(len(s)):
            if s[i] not in 'ab':
                ans += clear(st)
            else:
                st.append(s[i])
                if ''.join(st[-2:]) == pat[0]:
                    ans += val[0]
                    st.pop()
                    st.pop()
        ans += clear(st)
        return ans


cases = [
    ("cdbcbbaaabab", 4, 5, 19),
    ("aabbaaxybbaabb", 5, 4, 20),
    (
        "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha"
        , 1926,
        4320, 112374),

]
import aatest_helper

aatest_helper.run_test_cases(Solution().maximumGain, cases)
