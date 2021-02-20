package leetcode;

import java.util.Arrays;

class LCP18 {
    class Solution {
        public int breakfastNumber(int[] staple, int[] drinks, int x) {
            Arrays.sort(staple);
            Arrays.sort(drinks);
            int j = drinks.length - 1;
            int MOD = 1000000000 + 7;
            long ans = 0;
            for (int i = 0; i < staple.length; i++) {
                while (j >= 0 && (staple[i] + drinks[j] > x)) {
                    j -= 1;
                }
                ans += (j + 1);
                ans = ans % MOD;
            }
            return (int) ans;
        }
    }

    public static void main(String[] args) {
    }
}
