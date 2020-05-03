#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for t in tokens:
            if t in '+-*/':
                op2 = st.pop()
                op1 = st.pop()
                if t == '+':
                    v = op1 + op2
                elif t == '-':
                    v = op1 - op2
                elif t == '*':
                    v = op1 * op2
                elif t == '/':
                    v = int(op1 * 1.0 / op2)
                # print op1, op2, t , v
            else:
                v = int(t)
            st.append(v)
        return st[0]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
