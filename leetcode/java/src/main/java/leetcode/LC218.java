package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;

class LC218 {
    class Solution {
        class Event implements Comparable<Event> {
            int in;
            int x;
            int h;
            int idx;

            public Event(int in, int x, int h, int idx) {
                this.in = in;
                this.x = x;
                this.h = h;
                this.idx = idx;
            }

            public int compareTo(Event it) {
                return x - it.x;
            }
        }

        class Building implements Comparable<Building> {
            int h;
            int idx;

            public Building(int h, int idx) {
                this.h = h;
                this.idx = idx;
            }

            public int compareTo(Building it) {
                if (this.h != it.h) {
                    return this.h - it.h;
                }
                return this.idx - it.idx;
            }
        }

        public List<List<Integer>> getSkyline(int[][] buildings) {
            int n = buildings.length;
            List<List<Integer>> ans = new ArrayList<>();
            if (n == 0) {
                return ans;
            }

            Event[] events = new Event[2 * n];
            for (int i = 0; i < n; i++) {
                events[2 * i] = new Event(0, buildings[i][0], buildings[i][2], i);
                events[2 * i + 1] = new Event(1, buildings[i][1], buildings[i][2], i);
            }
            Arrays.sort(events);

            TreeSet<Building> ts = new TreeSet<>();
            int cur = events[0].x;

            for (int i = 0; i < events.length; i++) {
                Event ev = events[i];
                int h = 0;
                if (ts.size() > 0) {
                    h = ts.last().h;
                }
                if (ev.in == 0) {
                    if ((h < ev.h) && (ev.x > cur)) {
                        ArrayList<Integer> t = new ArrayList();
                        t.add(cur);
                        t.add(h);
                        cur = ev.x;
                        ans.add(t);
                    }
                    ts.add(new Building(ev.h, ev.idx));
                } else {
                    if ((h == ev.h) && (ev.x > cur)) {
                        ArrayList<Integer> t = new ArrayList();
                        t.add(cur);
                        t.add(h);
                        cur = ev.x;
                        ans.add(t);
                    }
                    ts.remove(new Building(ev.h, ev.idx));
                }
            }

            ArrayList<Integer> t = new ArrayList();
            t.add(cur);
            t.add(0);
            ans.add(t);

            List<List<Integer>> res = new ArrayList<>();
            for (int i = 0; i < ans.size(); i++) {
                int j = res.size();
                if ((j > 0) && res.get(j - 1).get(1).equals(ans.get(i).get(1))) {
                    continue;
                }
                res.add(ans.get(i));
            }

            return res;
        }
    }
}