import java.util.Arrays;
import java.util.HashMap;
import java.util.TreeSet;

class Solution {
    public int oddEvenJumps(int[] A) {
        HashMap<Integer, Integer> positions = new HashMap<Integer, Integer>();
        TreeSet<Integer> values = new TreeSet<Integer>();
        int[] odd_next = A.clone();
        int[] even_next = A.clone();

        for (int i = A.length - 1; i >= 0; i--) {
            int x = A[i];

            Integer v;
            v = values.ceiling(x);
            if (v != null) {
                odd_next[i] = positions.get(v);
            } else {
                odd_next[i] = -1;
            }

            v = values.floor(x);
            if (v != null) {
                even_next[i] = positions.get(v);
            } else {
                even_next[i] = -1;
            }

            values.add(x);
            positions.put(x, i);
        }

        // System.out.println(Arrays.toString(odd_next));
        // System.out.println(Arrays.toString(even_next));

        int[][] dp = new int[2][A.length];
        // dp[0][i] -> dp[1][j] where A[i] <= A[j]
        // dp[1][i] -> dp[0][j] where A[i]] >= A[j]
        for (int i = 0; i < A.length; i++) {
            dp[0][i] += 1;

            int j = odd_next[i];
            if (j != -1) {
                dp[1][j] += dp[0][i];
            }
            j = even_next[i];
            if (j != -1) {
                dp[0][j] += dp[1][i];
            }
        }
        // System.out.println(Arrays.toString(dp[0]));
        // System.out.println(Arrays.toString(dp[1]));

        int ans = dp[0][A.length - 1] + dp[1][A.length - 1];
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.oddEvenJumps(new int[] { 10, 13, 12, 14, 15 }));
        System.out.println(sol.oddEvenJumps(new int[] { 2, 3, 1, 1, 4 }));
        System.out.println(sol.oddEvenJumps(new int[] { 5, 1, 3, 4, 2 }));

    }
}