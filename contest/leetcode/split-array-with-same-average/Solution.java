import java.util.*;

import java.util.*;

class Solution {
    public boolean splitArraySameAverage(int[] A) {
        int n = A.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += A[i];
        }
        int[] dp = new int[sum + 1];
        dp[0] = 1;

        for (int k = 0; k < n; k++) {
            int x = A[k];
            for (int y = sum - x; y >= 0; y--) {
                // 这里直接移位就好
                // int c = dp[y];
                // int c2 = 0;
                // for (int i = 0; i < (n - 1); i++) {
                //     if ((c & (1 << i)) == 0)
                //         continue;

                //     c2 |= (1 << (i + 1));
                //     if (((x + y) * (n - i - 1)) == ((sum - x - y) * (i + 1))) {
                //         return true;
                //     }
                // }
                // dp[x + y] |= c2;
                dp[x + y] |= (dp[y] << 1);
            }
        }

        for (int k = 1; k < n; k++) {
            if ((sum * k) % n == 0) {
                int x = sum * k / n;
                if ((dp[x] & (1 << k)) != 0) {
                    return true;
                }
            }
        }
        return false;
    }
}