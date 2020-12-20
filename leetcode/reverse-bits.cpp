/* coding:utf-8
 * Copyright (C) dirlt
 */

#define uint32_t unsigned int

class Solution {
   public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t v = 0;
        for (int i = 0; i < 32; i++) {
            v = v << 1;
            v += (n & 0x1);
            n = n >> 1;
        }
        return v;
    }
};
