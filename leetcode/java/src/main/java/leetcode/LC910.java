package leetcode;

import java.util.Arrays;

class LC910 {
    class Solution {
        public int smallestRangeII(int[] A, int K) {
            Arrays.sort(A);
            int ans = A[A.length - 1] - A[0];
            for (int i = 0; i < A.length - 1; i++) {
                int minx = Math.min(A[0] + 2 * K, A[i + 1]);
                int maxx = Math.max(A[i] + 2 * K, A[A.length - 1]);
                ans = Math.min(ans, maxx - minx);
            }
            return ans;
        }
    }
}