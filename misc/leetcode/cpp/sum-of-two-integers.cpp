/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    int getSum(int a, int b) {
        while (a) {
            int c = (a & b) << 1;
            int d = a ^ b;
            a = c;
            b = d;
        }
        return b;
    }
};
