package com.dirlt.java.playground;

import java.util.HashMap;
import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 13-5-3
 * Time: 下午5:22
 * To change this template use File | Settings | File Templates.
 */
public class IndexValueAggregator {
    static class IndexValue implements Comparable<IndexValue> {
        private static final String kSeperator = "_";
        String index;
        Long value;
        Long[] args;

        public IndexValue(String index, Long value, Long[] args) {
            this.index = index;
            this.value = value;
            this.args = args;
        }

        @Override
        public int compareTo(IndexValue iv) {
            // reverse order.
            if (value < iv.value) {
                return 1;
            } else if (value == iv.value) {
                return -1;
            } else {
                return -1;
            }
        }

        public void append(StringBuilder sb) {
            sb.append(index);
            for (Long arg : args) {
                sb.append(kSeperator);
                sb.append(Long.toString(arg));
            }
        }
    }

    private String day;
    private java.util.Map<String, FixedSizeHeap<IndexValue>> db = new HashMap<String, FixedSizeHeap<IndexValue>>();
    private static final int kTopNumber = 200;
    private static final String kSeperator = "|";

    public IndexValueAggregator(String day) {
        this.day = day;
    }

    public void sink(String type, String index, String key, Long value, Long... args) {
        // models_1_day_installCnt_values
        // models_1_day_lanCnt_values.
        String k = type + "s_" + day + "_day_" + index + "_values";
        IndexValue indexValue = new IndexValue(key, value, args);
        FixedSizeHeap<IndexValue> pq = db.get(k);
        if (pq == null) {
            pq = new FixedSizeHeap<IndexValue>(kTopNumber);
            db.put(k, pq);
        }
        System.out.println("add key " + k + ", index value " + key + ", " + value);
        pq.add(indexValue);
    }

    public void doOutput() {
        for (String key : db.keySet()) {
            StringBuilder sb = new StringBuilder();
            FixedSizeHeap<IndexValue> pq = db.get(key);
            Iterator<IndexValue> iterator = pq.iterator();
            int count = 0;
            while (iterator.hasNext()) {
                if (count != 0) {
                    sb.append(kSeperator);
                }
                count++;
                IndexValue iv = iterator.next();
                iv.append(sb);
            }
            System.out.println("output key = " + key + ", value = " + sb.toString());
        }
    }

    public static void main(String[] args) {
        IndexValueAggregator iv = new IndexValueAggregator("1");
        iv.sink("osVersion","installCnt","100",(long)1,(long)1,(long)2);
        iv.sink("osVersion","installCnt","101",(long)2,(long)2,(long)1);
        iv.sink("osVersion","installCnt","102",(long)2,(long)2,(long)1);
        iv.doOutput();
    }

}
