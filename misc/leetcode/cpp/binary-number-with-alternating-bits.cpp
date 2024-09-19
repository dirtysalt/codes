/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    bool hasAlternatingBits(int n) {
        int next = (n & 0x1);
        while (n) {
            if ((n & 0x1) != next) {
                return false;
            }
            next = 1 - next;
            n = n >> 1;
        }
        return true;
    }
};
