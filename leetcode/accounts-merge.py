#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

import aatest_helper


class FindUnion:
    def __init__(self, size):
        self.roots = [-1] * size

    def find_parent(self, c):
        p = c
        while self.roots[p] != -1:
            p = self.roots[p]

        x = c
        while self.roots[x] != -1:
            y = self.roots[x]
            self.roots[x] = p
            x = y

        return p

    def set_parent(self, c, p):
        self.roots[c] = p

    def all_parents(self):
        res = []
        for v in range(len(self.roots)):
            if self.roots[v] == -1:
                res.append(v)
        return res


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = []
        email_to_idx = {}
        list_of_email = []
        groups = []
        for acc in accounts:
            name, emails = acc[0], acc[1:]
            values = []
            for email in emails:
                if email not in email_to_idx:
                    email_to_idx[email] = len(list_of_email)
                    list_of_email.append(email)
                    names.append(name)
                idx = email_to_idx[email]
                values.append(idx)
            values.sort()
            groups.append(values)

        fu = FindUnion(len(list_of_email))

        for values in groups:
            if len(values) == 1:
                continue
            p = fu.find_parent(values[0])
            for v in values[1:]:
                p2 = fu.find_parent(v)
                if p == p2:
                    continue
                fu.set_parent(p2, p)

        ps = fu.all_parents()
        res = {k: {'name': names[k], 'emails': []} for k in ps}

        for idx, email in enumerate(list_of_email):
            p = fu.find_parent(idx)
            res[p]['emails'].append(email)

        ans = []
        for v in res.values():
            name = v['name']
            emails = v['emails']
            emails.sort()
            ans.append([name] + emails)
        return ans


cases = [
    ([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
      ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
     [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"],
      ["Mary", "mary@mail.com"]]),

    ([["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"], ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
      ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"], ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
      ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]],
     [['Alex', 'Alex0@m.co', 'Alex4@m.co', 'Alex5@m.co'], ['Ethan', 'Ethan0@m.co', 'Ethan3@m.co'],
      ['Kevin', 'Kevin2@m.co', 'Kevin4@m.co'], ['Gabe', 'Gabe0@m.co', 'Gabe2@m.co', 'Gabe3@m.co', 'Gabe4@m.co']])
]

sol = Solution()
aatest_helper.run_test_cases(sol.accountsMerge, cases)
