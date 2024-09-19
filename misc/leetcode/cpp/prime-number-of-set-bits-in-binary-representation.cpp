/* coding:utf-8
 * Copyright (C) dirlt
 */

class Solution {
   public:
    int countPrimeSetBits(int L, int R) {
        const int max_bits = 32;
        char nprimes[max_bits + 1] = {0};
        for (int k = 2; (k * k) <= max_bits; k++) {
            if (nprimes[k] == 1) continue;
            for (int r = 2; (r * k) <= max_bits; r++) {
                nprimes[r * k] = 1;
            }
        }
        int result = 0;
        for (int n = L; n <= R; n++) {
            int c = 0;
            int v = n;
            while (v) {
                c += (v & 0x1);
                v = v >> 1;
            }
            if (c == 0 || c == 1) continue;
            if (nprimes[c] == 0) {
                result += 1;
            }
        }
        return result;
    }
};
