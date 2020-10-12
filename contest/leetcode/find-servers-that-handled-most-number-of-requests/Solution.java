package org.aap.examples;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.TreeSet;

class Solution {
    class Event implements Comparable<Event> {
        int time;
        int op; // 0 new load, 1 server are available.
        int index;
        int serverId;

        @Override
        public int compareTo(final Event o) {
            if (this.time != o.time) {
                return this.time - o.time;
            }
            // server available higher priority
            return -(this.op - o.op);
        }
    }

    static void Debug(String format, Object... args) {
//        System.out.printf(format + "\n", args);
    }

    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        PriorityQueue<Event> events = new PriorityQueue<>();
        for (int i = 0; i < arrival.length; i++) {
            Event ev = new Event();
            ev.time = arrival[i];
            ev.op = 0;
            ev.index = i;
            events.add(ev);
        }
        int[] serverLoads = new int[k];
        TreeSet<Integer> servers = new TreeSet<>();
        for (int i = 0; i < k; i++) {
            servers.add(i);
        }
        while (!events.isEmpty()) {
            Event ev = events.remove();
            if (ev.op == 0) {
                int index = ev.index;
                int cost = load[index];
                // find available servers.
                Integer idx = servers.ceiling(index % k);
                if (idx == null && !servers.isEmpty()) {
                    idx = servers.first();
                }
                if (idx == null) {
                    Debug("drop req#%d", index);
                    continue;
                }
                Debug("req#%d on server#%d", index, idx);
                serverLoads[idx] += 1;
                servers.remove(idx);
                Event ev2 = new Event();
                ev2.time = ev.time + cost;
                ev2.op = 1;
                ev2.serverId = idx;
                events.add(ev2);
            } else {
                int serverId = ev.serverId;
                servers.add(serverId);
                Debug("release server#%d", serverId);
            }
        }
        Debug(Arrays.toString(serverLoads));
        int maxLoad = Arrays.stream(serverLoads).max().getAsInt();
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (serverLoads[i] == maxLoad) {
                ans.add(i);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.busiestServers(3, new int[]{1, 2, 3, 4, 5}, new int[]{5, 2, 3, 3, 3}));
        System.out.println(sol.busiestServers(3, new int[]{1, 2, 3, 4}, new int[]{1, 2, 1, 2}));
        System.out.println(sol.busiestServers(3, new int[]{1, 2, 3}, new int[]{10, 12, 11}));
        System.out.println(sol.busiestServers(3, new int[]{1, 2, 3, 4, 8, 9, 10}, new int[]{5, 2, 10, 3, 1, 2, 2}));
        System.out.println(sol.busiestServers(2, new int[]{1, 2, 3}, new int[]{1000000000, 1, 1000000000}));
    }
}