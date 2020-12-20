package leetcode;

import java.util.Arrays;
import java.util.TreeSet;

public class LC757 {
    class Solution {
        class Pair implements Comparable<Pair> {
            int s;
            int e;

            @Override
            public int compareTo(final Pair pair) {
                if (e != pair.e) {
                    return e - pair.e;
                }
                return s - pair.e;
            }
        }

        public int intersectionSizeTwo(int[][] intervals) {
            Pair[] ps = new Pair[intervals.length];
            for (int i = 0; i < intervals.length; i++) {
                Pair p = new Pair();
                p.s = intervals[i][0];
                p.e = intervals[i][1];
                ps[i] = p;
            }
            Arrays.sort(ps);

            TreeSet<Integer> ts = new TreeSet<>();
            ts.add(ps[0].e);
            ts.add(ps[0].e - 1);
            for (int i = 1; i < ps.length; i++) {
                Integer a = ts.last();
                Integer b = ts.floor(a - 1);
                if (a == ps[i].s) {
                    // b a
                    //   s e
                    ts.add(ps[i].e);
                } else if (a < ps[i].s) {
                    // b a
                    //      s e
                    ts.add(ps[i].e);
                    ts.add(ps[i].e - 1);
                } else if (a == ps[i].e) {
                    // b    a
                    //   s  e
                    if (b < ps[i].s) {
                        ts.add(ps[i].e - 1);
                    }
                } else {
                    assert a < ps[i].e;
                    if (b < ps[i].s) {
                        // b   a
                        //   s   e
                        // 这种情况可能存在
                        // 我们依然把e加入
                        // 因为从贪心角度来说，加入e更有可能覆盖到下一个区间
                        ts.add(ps[i].e);
                    }
                }
            }
//            System.out.println(Arrays.toString(ts.toArray()));
            return ts.size();
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC757().new Solution();
        {
            int[][] intervals = {{1, 3}, {1, 4}, {2, 5}, {3, 5}};
            System.out.println(sol.intersectionSizeTwo(intervals));
        }
        {
            int[][] intervals = {{1, 2}, {2, 3}, {2, 4}, {4, 5}};
            System.out.println(sol.intersectionSizeTwo(intervals));
        }
        {
            int[][] intervals = {{8, 9}, {4, 21}, {3, 19}, {5, 9}, {1, 5}};
            System.out.println(sol.intersectionSizeTwo(intervals));
        }
    }
}
