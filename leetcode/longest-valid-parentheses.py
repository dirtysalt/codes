#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        st = []
        match = [-1] * n
        for i in range(n):
            c = s[i]
            if c == '(':
                st.append(i)
            else:
                if st:
                    match[i] = st[-1]
                    st.pop()

        dp = [0] * n
        for i in range(n):
            if s[i] == ')':
                m = match[i]
                if m != -1:
                    dp[i] = (i - m + 1) + dp[m - 1]
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses(")()())()()("))
    print(sol.longestValidParentheses(')()())'))
    print(sol.longestValidParentheses('()()'))
    print(sol.longestValidParentheses('(()'))
    print(sol.longestValidParentheses('()(()'))
    print(sol.longestValidParentheses("(()(((()"))
    print(sol.longestValidParentheses('(())(()))))(((((((()()))())'))
