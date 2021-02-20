/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    int rangeBitwiseAnd(int m, int n) {
        int res = 0;
        // 如果最大值和最小值在某个个位置上bit都是1
        // 并且这个位置的更高位相同的话，说明这个区间内所有的数
        // 在这个位置上可以保持bit = 1
        for (int bit = 30; bit >= 0; bit--) {
            int mb = (m >> bit);
            int nb = (n >> bit);
            if ((mb & 0x1) && (nb & 0x1) && (mb == nb)) {
                res |= (1 << bit);
            }
        }
        return res;
    }
};
