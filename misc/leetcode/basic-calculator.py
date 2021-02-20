#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = [[]]

        def eval_ops(ops):
            # print(ops)
            val = ops[0]
            for i in range(1, len(ops), 2):
                op = ops[i]
                x = ops[i + 1]
                if op == '+':
                    val = val + x
                else:
                    val = val - x
            return val

        i = 0
        while i < len(s):
            c = s[i]

            if c == ' ':
                pass
            elif c == '+' or c == '-':
                st[-1].append(c)
            elif c == '(':
                st.append([])
            elif c == ')':
                ops = st[-1]
                st.pop()
                res = eval_ops(ops)
                st[-1].append(res)
            else:
                val = 0
                while i < len(s) and s[i] in string.digits:
                    val = val * 10 + ord(s[i]) - ord('0')
                    i += 1
                i -= 1
                st[-1].append(val)

            i += 1

        ops = st[-1]
        st.pop()
        ans = eval_ops(ops)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('(1+(4+5+2)-3)+(6+8)'))
    print(sol.calculate('1+2'))
