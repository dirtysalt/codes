#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = {}
        target = 0
        for x in req_skills:
            value = len(skills)
            skills[x] = value
            target |= (1 << value)

        pp = []
        for xs in people:
            res = 0
            for x in xs:
                value = skills.get(x)
                if value is None:
                    continue
                res |= (1 << value)
            pp.append(res)
        assert len(pp) == len(people)

        inf = 1 << 20
        dp = [inf] * (target + 1)
        path = [None] * (target + 1)
        dp[0] = 0
        for t in range(target):
            x = dp[t]
            for i, p in enumerate(pp):
                y = t | p
                if (x + 1) < dp[y]:
                    dp[y] = x + 1
                    path[y] = (i, t)

        assert dp[target] != inf
        ans = []
        t = target
        while t != 0:
            i, t2 = path[t]
            ans.append(i)
            t = t2
        ans.sort()
        return ans


cases = [
    (["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]], [0, 2]),
    (["algorithms", "math", "java", "reactjs", "csharp", "aws"],
     [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
      ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]], [1, 2]),
    (["hdbxcuzyzhliwv", "uvwlzkmzgis", "sdi", "bztg", "ylopoifzkacuwp", "dzsgleocfpl"],
     [["hdbxcuzyzhliwv", "dzsgleocfpl"], ["hdbxcuzyzhliwv", "sdi", "ylopoifzkacuwp", "dzsgleocfpl"],
      ["bztg", "ylopoifzkacuwp"], ["bztg", "dzsgleocfpl"], ["hdbxcuzyzhliwv", "bztg"], ["dzsgleocfpl"], ["uvwlzkmzgis"],
      ["dzsgleocfpl"], ["hdbxcuzyzhliwv"], [], ["dzsgleocfpl"], ["hdbxcuzyzhliwv"], [],
      ["hdbxcuzyzhliwv", "ylopoifzkacuwp"], ["sdi"], ["bztg", "dzsgleocfpl"],
      ["hdbxcuzyzhliwv", "uvwlzkmzgis", "sdi", "bztg", "ylopoifzkacuwp"], ["hdbxcuzyzhliwv", "sdi"],
      ["hdbxcuzyzhliwv", "ylopoifzkacuwp"], ["sdi", "bztg", "ylopoifzkacuwp", "dzsgleocfpl"], ["dzsgleocfpl"],
      ["sdi", "ylopoifzkacuwp"], ["hdbxcuzyzhliwv", "uvwlzkmzgis", "sdi"], [], [], ["ylopoifzkacuwp"], [],
      ["sdi", "bztg"], ["bztg", "dzsgleocfpl"], ["sdi", "bztg"]], [19, 22])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestSufficientTeam, cases)
