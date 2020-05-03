/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cmath>
#include <vector>
using namespace std;
class Solution {
   public:
    int countPrimes(int n) {
        if (n == 0) return 0;
        n -= 1;
        if (n <= 1) return 0;
        if (n == 2) return 1;
        vector<char> primes(n + 1);
        int upper = lround(sqrt(n)) + 2;
        for (int i = 2; i <= upper; i++) {
            int upper2 = n / i;
            for (int j = i; j <= upper2; j++) {
                primes[i * j] = 1;
            }
        }
        int ans = 1;
        for (int i = 3; i <= n; i++) {
            if (primes[i] == 0) {
                ans += 1;
            }
        }
        return ans;
    }
};