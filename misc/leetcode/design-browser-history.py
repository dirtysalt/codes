#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.st = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.st = self.st[:self.pos + 1]
        self.pos += 1
        self.st.append(url)

    def back(self, steps: int) -> str:
        self.pos -= steps
        self.pos = max(self.pos, 0)
        return self.st[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += steps
        self.pos = min(self.pos, len(self.st) - 1)
        return self.st[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

null = None
cases = [
    (["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"],
     [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [
         7]],
     [null, null, null, null, "facebook.com", "google.com", "facebook.com", null, "linkedin.com", "google.com",
      "leetcode.com"]),
]

import aatest_helper

aatest_helper.run_simulation_cases(BrowserHistory, cases)
