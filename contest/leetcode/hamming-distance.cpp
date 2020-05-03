/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int dist = 0;
        while (z) {
            dist += (z & 0x1);
            z = z >> 1;
        }
        return dist;
    }
};
