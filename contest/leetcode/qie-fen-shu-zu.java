import java.util.*;

class Solution {
    public int splitArray(int[] nums) {
        int M = 1000000;
        int factors[] = new int[M + 1];
        for (int i = 2; i <= M; i++) {
            if (factors[i] != 0)
                continue;
            for (int j = i; j <= M; j += i) {
                factors[j] = i;
            }
        }

        final int inf = 1 << 30;
        int dp[] = new int[M + 1];
        Arrays.fill(dp, inf);

        int ans = 0;
        for (int x : nums) {
            int res = ans + 1;
            while (x > 1) {
                int f = factors[x];
                dp[f] = Math.min(dp[f], ans);
                res = Math.min(dp[f] + 1, res);
                while ((x % f) == 0) {
                    x = x / f;
                }
            }
            ans = res;
        }
        return ans;
    }
}
