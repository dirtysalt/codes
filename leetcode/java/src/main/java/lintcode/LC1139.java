package lintcode;

// https://www.lintcode.com/problem/the-kth-subarray/description

class LC1139 {
    public class Solution {
        /**
         * @param a: an array
         * @param k: the kth
         * @return: return the kth subarray
         */
        public long find_rank(long[] tmp, long value) {
            long res = 0;
            int j = 0;
            for (int i = 0; i < tmp.length; i++) {
                while ((j < tmp.length) && ((tmp[j] - tmp[i]) <= value)) {
                    j += 1;
                }
                j -= 1;
                res += (j - i);
            }
            return res;
        }

        public long thekthSubarray(int[] a, long k) {
            // wrrite your code here
            long[] tmp = new long[a.length + 1];
            long amin = 0, asum = 0;
            for (int i = 0; i < a.length; i++) {
                tmp[i + 1] = tmp[i] + a[i];
                amin = Math.min(amin, a[i]);
                asum += a[i];
            }

            long s = amin, e = asum;
            while (s <= e) {
                long m = (e - s) / 2 + s;
                long rank = find_rank(tmp, m);
                if (rank >= k) {
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            }
            return s;
        }
    }
}
