package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeMap;

public class LC1383 {

    class Solution {
        class Pair<T, U> {
            T first;
            U second;

            Pair(T t, U u) {
                first = t;
                second = u;
            }
        }

        class MyMap {
            TreeMap<Integer, Integer> data = new TreeMap<>();

            void add(int x) {
                Integer p = data.get(x);
                if (p == null) {
                    p = 0;
                }
                data.put(x, p + 1);
            }

            void remove(int x) {
                Integer p = data.get(x);
                if (p == 1) {
                    data.remove(x);
                } else {
                    data.put(x, p - 1);
                }
            }

            Integer below(int x) {
                return data.floorKey(x);
            }

            boolean existed(int x) {
                return data.get(x) != null;
            }
        }


        public void debug(String message) {
            System.out.println(message);
        }

        public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
            ArrayList<Pair<Integer, Integer>> ps = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                Pair<Integer, Integer> p = new Pair<>(efficiency[i], speed[i]);
                ps.add(p);
            }
            ps.sort(new Comparator<Pair<Integer, Integer>>() {
                @Override
                public int compare(final Pair<Integer, Integer> t0, final Pair<Integer, Integer> t1) {
                    if (t0.first == t1.first) {
                        return t0.second - t1.second;
                    }
                    return t0.first - t1.first;
                }
            });

            MyMap alt = new MyMap();
            MyMap used = new MyMap();
            Arrays.sort(speed);
            long speedSum = 0; // max k-1 items.
            for (int i = 1; i < k; i++) {
                int s = speed[n - i];
                speedSum += s;
                used.add(s);
            }
            for (int i = k; i <= n; i++) {
                int s = speed[n - i];
                alt.add(s);
            }


            long ans = 0;
            for (int i = 0; i < n; i++) {
                int e = ps.get(i).first;
                int s = ps.get(i).second;
                // check s is already in used.
                // if yes, then remove it and add lower/eq one.
                if (used.existed(s)) {
                    used.remove(s);
                    speedSum -= s;

                    Integer s2 = alt.below(s);
                    if (s2 != null) {
                        alt.remove(s2);
                        used.add(s2);
                        speedSum += s2;
                    }
                } else {
                    alt.remove(s);
                }
//                debug(String.format("s = %d, e = %d, speedSum+s = %d", s, e, speedSum + s));
                long value = (speedSum + s) * e;
                ans = Math.max(ans, value);
            }
            int MOD = 1000000000 + 7;
            return (int) (ans % MOD);
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC1383().new Solution();
        {
            int[] speed = {2, 10, 3, 1, 5, 8};
            int[] eff = {5, 4, 3, 9, 7, 2};
            System.out.println(sol.maxPerformance(6, speed, eff, 2));
        }
        {
            int[] speed = {2, 10, 3, 1, 5, 8};
            int[] eff = {5, 4, 3, 9, 7, 2};
            System.out.println(sol.maxPerformance(6, speed, eff, 3));
        }
        {
            int[] speed = {2, 10, 3, 1, 5, 8};
            int[] eff = {5, 4, 3, 9, 7, 2};
            System.out.println(sol.maxPerformance(6, speed, eff, 4));
        }
    }
}
