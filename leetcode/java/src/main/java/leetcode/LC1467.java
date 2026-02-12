package leetcode;

class LC1467 {
    class Solution {
        private long tt, ok;
        private int n, N;
        private int[][] C;
        private int[] balls;

        public void search(int i, int k, int diff, long value) {
            if (i == n) {
                if (k != N) {
                    return;
                }
                tt += value;
                if (diff == 0) {
                    ok += value;
                }
                return;
            }

            int rest = 0;
            for (int j = i; j < n; j++) {
                rest += balls[j];
            }
            if ((k + rest) < N) {
                return;
            }
            for (int c = 0; c <= balls[i]; c++) {
                if ((k + c) > N) {
                    break;
                }
                long v = value * C[balls[i]][c];
                int df = diff;
                if (c == 0) {
                    df += 1;
                } else if (c == balls[i]) {
                    df -= 1;
                }
                search(i + 1, k + c, df, v);
            }
            return;
        }

        public double getProbability(int[] balls) {
            this.balls = balls;
            tt = 0;
            ok = 0;

            n = balls.length;
            N = 0;
            for (int x : balls) {
                N += x;
            }
            N = N / 2;
            C = new int[10][];
            for (int i = 0; i < 10; i++) {
                C[i] = new int[10];
                C[i][0] = 1;
                for (int j = 1; j <= i; j++) {
                    C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
                }
                // System.out.println(i + Arrays.toString(C[i]));
            }
            search(0, 0, 0, 1);
            double ans = ok * 1.0 / tt;
            return ans;
        }
    }

    public static void main(String[] args) {
        LC1467 inst = new LC1467();
        Solution sol = inst.new Solution();
        int[] balls = {6, 6, 6, 6, 6, 6};
        System.out.println(sol.getProbability(balls));
    }
}