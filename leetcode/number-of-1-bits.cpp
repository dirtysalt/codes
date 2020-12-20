/* coding:utf-8
 * Copyright (C) dirlt
 */

#define uint32_t unsigned int

class Solution {
   public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            count += (n & 0x1);
            n = n >> 1;
        }
        return count;
    }
};
