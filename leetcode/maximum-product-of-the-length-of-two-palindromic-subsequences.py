#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        states = [0] * (1 << n)
        for st in range(1 << n):
            idx = []
            for i in range(st):
                if (st >> i) & 0x1:
                    idx.append(i)
            i, j = 0, len(idx) - 1
            ok = True
            while i <= j:
                if s[idx[i]] != s[idx[j]]:
                    ok = False
                    break
                i += 1
                j -= 1
            if ok:
                states[st] = len(idx)

        ans = 0
        for st in range(1 << n):
            if states[st] == 0: continue
            mask = (1 << n) - 1 - st
            c = mask
            while True:
                c = c & mask
                if c == 0: break
                ans = max(ans, states[st] * states[c])
                c -= 1
        return ans


"""
class Solution {
public:
    int maxProduct(string s) {
        size_t n = s.size();
        std::vector<int> states((1<< n), 0);
        
        for(int st = 0; st < (1 << n); st ++) {
            std::vector<int> pos;
            for (int i=0;i<n;i++) {
                if ((st >> i) & 0x1) {
                    pos.push_back(i);
                }
            }
            int i=0, j = pos.size()-1;
            bool ok = true;
            while(i <= j) {
                if (s[pos[i]] != s[pos[j]]) {
                    ok = false;
                    break;
                }
                i += 1;
                j -= 1;
            }
            if (ok) {
                states[st] = pos.size();
            }
        }

        int ans = 0;

        for(int st =0;st < (1 << n);st++) {
            if(states[st] == 0) continue;
            int mask = (1 << n) - 1 - st;
            int c = mask;
            for(;;) {
                c = c & mask;
                if (c == 0) break;
                ans = std::max(ans, states[st] * states[c]);
                c -= 1;                
            }
        }
        return ans;
    }
};
"""

true, false, null = True, False, None
cases = [
    ("nnwwwwwnnnwn", 36),
    ("leetcodecom", 9),
    ("bb", 1),
    ("accbcaxxcxx", 25),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProduct, cases)

if __name__ == '__main__':
    pass
