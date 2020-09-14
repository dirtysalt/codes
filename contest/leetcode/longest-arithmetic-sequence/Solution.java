class Item implements Comparable<Item> {
    int value;
    int index;
    public Item(int value, int index) {
        this.value = value;
        this.index = index;
    }
    public int compareTo(Item x) {
        if (value != x.value) {
            return value - x.value;
        }
        return index  - x.index;
    }
    public String toString() {
        return String.format("(value=%d, index=%d)", value, index);
    }
}
class Solution {
    public int longestArithSeqLength(int[] A) {
        TreeSet<Item> ts = new TreeSet<>();
        for (int i = 0; i < A.length; i++ ){
            int x = A[i];
            ts.add(new Item(x,i));
        }
        int[][]visited = new int[A.length][];
        for(int i=0;i<A.length;i++) {
            visited[i] = new int[A.length];
        }
        int ans = 2;
        for(int i=0;i<A.length;i++) {
            for (int j=i+1;j<A.length;j++) {
                if (visited[i][j] == 1) {
                    continue;
                }
                visited[i][j] = 1;
                int d = A[j] - A[i];
                int exp = A[j] + d;
                int sz = 2;
                int k = j;
                while (true) {
                    Item x = ts.ceiling(new Item(exp, k+1));
                    // System.out.printf("search item. exp = %d, k+1 = %d, x = %s\n", exp, k+1, x);
                    if (x != null && x.value == exp) {
                        sz += 1;
                        exp += d;
                        int k2 = x.index;
                        visited[k][k2] = 1;
                        k = k2;
                    } else {
                        break;
                    }
                }
                ans = Math.max(ans, sz);
            }
        }
        return ans;
    }
}