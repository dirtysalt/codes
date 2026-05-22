#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """

#         # to match 'a*' or '.*' against empty string
#         s = '#' + s
#         # add prefix to avoid index error.
#         p = '^' + p
#         st = []
#         for i in range(len(s)):
#             st.append([0] * len(p))
#         self.st = st
#         st[0][0] = 1

#         for i in range(0, len(s)):
#             for j in range(1, len(p)):
#                 def cmatch():
#                     return p[j] == '*' or \
#                       (p[j] == '?' and i != 0) or \
#                       (p[j] == s[i])

#                 if not cmatch():
#                     continue

#                 if (p[j] == '?' and i != 0) or p[j] == s[i]:
#                     st[i][j] = st[i-1][j-1]
#                 else:
#                     for x in range(i, -1, -1):
#                         if st[x][j-1]:
#                             st[i][j] = 1
#                             break

#         return bool(st[len(s)-1][len(p)-1])

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """

#         # to match 'a*' or '.*' against empty string
#         s = '#' + s
#         # add prefix to avoid index error.
#         p = '^' + p
#         st = []
#         for i in range(len(s)):
#             st.append([0] * len(p))
#         self.st = st
#         st[0][0] = 1

#         for j in range(1, len(p)):
#             if p[j] == '*':
#                 v = 0
#                 for i in range(0, len(s)):
#                     v |= st[i][j-1]
#                     st[i][j] = v

#             else:
#                 for i in range(1, len(s)):
#                     if p[j] == s[i] or p[j] == '?':
#                         st[i][j] = st[i-1][j-1]

#         return bool(st[len(s)-1][len(p)-1])

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """

#         # to match 'a*' or '.*' against empty string
#         s = '#' + s
#         # add prefix to avoid index error.
#         p = '^' + p
#         st = []
#         for i in range(2):
#             st.append([0] * len(s))
#         self.st = st
#         st[0][0] = 1
#         swt = 0

#         for j in range(1, len(p)):
#             aft = 1 - swt
#             if p[j] == '*':
#                 v = 0
#                 for i in range(0, len(s)):
#                     v |= st[swt][i]
#                     st[aft][i] = v

#             else:
#                 st[1-swt][0] = 0
#                 for i in range(1, len(s)):
#                     if p[j] == s[i] or p[j] == '?':
#                         st[aft][i] = st[swt][i-1]
#                     else:
#                         st[aft][i] = 0
#             swt = 1- swt
#             # print st

#         return bool(st[swt][len(s)-1])

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s = '#' + s

        # 把正则表达式按照*分割成为多块
        # 这样如果里面有长字符串的话
        # 可以直接进行匹配，而不用按照字符逐个去尝试

        ps = ['#']
        sub = ''
        for c in p:
            if c == '*':
                if sub:
                    ps.append(sub)
                    sub = ''
                ps.append('*')
            else:
                sub = sub + c
        if sub:
            ps.append(sub)
        # print ps, s

        st = []
        for i in range(2):
            st.append([0] * len(s))
        self.st = st
        st[0][0] = 1
        swt = 0

        for j in range(1, len(ps)):
            aft = 1 - swt
            if ps[j] == '*':
                v = 0
                for i in range(0, len(s)):
                    v |= st[swt][i]
                    st[aft][i] = v
            else:
                for i in range(0, len(s)):
                    st[aft][i] = 0
                ps_size = len(ps[j])
                for i in range(1, len(s) + 1 - ps_size):
                    end = i + ps_size - 1
                    if self.string_match(s[i: i + ps_size], ps[j]):
                        st[aft][end] = st[swt][i - 1]
                    else:
                        st[aft][end] = 0
            swt = aft
            # print st

        return bool(st[swt][len(s) - 1])

    def string_match(self, a, b):
        # print('a = {}, b = {}'.format(a, b))
        for (i, x) in enumerate(a):
            y = b[i]
            if y != '?' and x != y:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("abc", "abc*defghijk"))
    print(s.isMatch("aa", "aa"))
    print(s.isMatch("aa", "*"))
    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("ab", "?*"))
    print(s.isMatch("", "?"))
    print(s.isMatch("b", "*?*?"))
    print(s.isMatch('a' * 5000, '*' + 'a' * 4999 + '*'))
