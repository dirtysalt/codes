/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    int findComplement(int num) {
        int p = 0;
        int r = 0;
        while (num) {
            r += (1 - (num & 0x1)) << p;
            p += 1;
            num = num >> 1;
        }
        return r;
    }
};
