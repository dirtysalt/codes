/* coding:utf-8
 * Copyright (C) dirlt
 */

#define LL long long
class Solution {
   public:
    LL gcd(LL a, LL b) {
        while (true) {
            LL c = a % b;
            if (c == 0) {
                break;
            }
            a = b;
            b = c;
        }
        return b;
    }
    int uniquePaths(int m, int n) {
        LL a = 1, b = 1;
        for (int i = 1; i < n; i++) {
            a *= (LL)(m + i - 1);
            b *= (LL)i;
            LL c = gcd(a, b);
            a = a / c;
            b = b / c;
        }
        return (int)(a / b);
    }
};
