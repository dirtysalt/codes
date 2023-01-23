package leetcode;

public class LC1572 {
    class Solution {
        public int diagonalSum(int[][] mat) {
            int n = mat.length;
            int ans = 0;
            for (int i = 0; i < n; i++) {
                ans += mat[i][i];
                ans += mat[i][n - 1 - i];
            }
            if (n % 2 == 1) {
                int half = n / 2;
                ans -= mat[half][half];
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC1572().new Solution();
        {
            int[][] mat = {{1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9}};
            System.out.println(sol.diagonalSum(mat));
        }
        {
            int[][] mat = {{5}};
            System.out.println(sol.diagonalSum(mat));
        }
    }
}
