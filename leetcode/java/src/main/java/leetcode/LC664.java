package leetcode;

class LC664 {
    class Solution {
        int[][][] dp;

        public int query(char[] cs, int i, int j, int c) {
            if (i > j) {
                return 0;
            }
            int ans = dp[i][j][c];
            if (ans != -1) {
                return ans;
            }
            ans = 1 << 30;
            int k = i;
            while ((k <= j) && (cs[k] == cs[i])) {
                k += 1;
            }
            if (cs[i] == c) {
                ans = query(cs, k, j, c);
            } else {
                for (int k2 = k; k2 <= j + 1; k2++) {
                    int res = 1 + query(cs, k, k2 - 1, cs[i]) + query(cs, k2, j, c);
                    ans = Math.min(ans, res);
                }
            }
            dp[i][j][c] = ans;
            return ans;
        }

        public int strangePrinter(String s) {
            int n = s.length();
            if (n == 0) {
                return 0;
            }
            char[] cs = s.toCharArray();
            for (int i = 0; i < cs.length; i++) {
                cs[i] -= 'a';
            }
            dp = new int[n][n][26];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int c = 0; c < 26; c++) {
                        dp[i][j][c] = -1;
                    }
                }
            }
            int ans = query(cs, 0, n - 1, cs[0]) + 1;
            return ans;
        }
    }
}