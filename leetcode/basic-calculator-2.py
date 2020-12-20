#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def calculate(self, s: str) -> int:

        def unwind(st):
            # print(st)
            ans = st[0]
            for i in range(1, len(st), 2):
                if st[i] == '+':
                    ans += st[i + 1]
                else:
                    ans -= st[i + 1]
            return ans

        sst = []
        st = []

        i = 0
        while i < len(s):
            c = s[i]
            i += 1

            if c == ' ':
                continue

            # 对(单独开辟一个栈进行计算
            if c == '(':
                sst.append(st)
                st = []

            # 数字单独解析比较好
            elif c.isdigit():
                v = 0
                i -= 1
                while i < len(s) and s[i].isdigit():
                    v = v * 10 + ord(s[i]) - ord('0')
                    i += 1
                st.append(v)

            elif c == ')':
                res = unwind(st)
                st = sst.pop()
                st.append(res)

            else:
                # operator.
                st.append(c)

        ans = unwind(st)
        return ans
