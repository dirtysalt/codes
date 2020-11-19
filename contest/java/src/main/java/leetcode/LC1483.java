package leetcode;

import java.util.TreeMap;

class LC1483 {
    class TreeAncestor {
        private TreeMap<Integer, TreeMap<Integer, Integer>> dp;
        private int[] parent;
        private int n;

        public TreeAncestor(int n, int[] parent) {
            this.n = n;
            this.parent = parent;
            this.dp = new TreeMap();
        }

        public int getKthAncestor(int node, int k) {
            if (node == -1) {
                return -1;
            }
            if (k == 0) {
                return node;
            }
            Integer ans = -2;
            TreeMap<Integer, Integer> tm = dp.get(node);
            if (tm != null) {
                Integer t = tm.lowerKey(k);
                if (t != null) {
                    ans = getKthAncestor(tm.get(t), k - t);
                }
            } else {
                tm = new TreeMap();
                dp.put(node, tm);
            }
            if (ans == -2) {
                ans = getKthAncestor(parent[node], k - 1);
            }
            tm.put(k, ans);
            return ans;
        }
    }
}