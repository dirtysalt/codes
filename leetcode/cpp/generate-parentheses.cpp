/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
   public:
    struct Paren {
        int left;
        int right;
        string value;
        Paren(int l, int r, string v) {
            left = l;
            right = r;
            value = v;
        }
    };
    vector<string> generateParenthesis(int n) {
        vector<Paren> res;
        res.push_back(Paren(1, 0, "("));
        while (true) {
            vector<Paren> res2;
            for (int i = 0; i < res.size(); i++) {
                const Paren& p = res[i];
                if (p.left == p.right) {
                    if (p.left != n) {
                        res2.push_back(
                            Paren(p.left + 1, p.right, p.value + "("));
                    }
                } else {
                    if (p.left < n) {
                        res2.push_back(
                            Paren(p.left + 1, p.right, p.value + "("));
                    }
                    res2.push_back(Paren(p.left, p.right + 1, p.value + ")"));
                }
            }
            if (res2.size() == 0) break;
            res = res2;
        }
        vector<string> res2;
        for (int i = 0; i < res.size(); i++) {
            res2.push_back(res[i].value);
        }
        return res2;
    }
};
