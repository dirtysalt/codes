package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.util.Bytes;

import java.util.Arrays;
import java.util.Iterator;
import java.util.Map;
import java.util.NavigableMap;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 2/19/13
 * Time: 5:27 PM
 * To change this template use File | Settings | File Templates.
 */
    public class CompareHBaseTable {
    public static void main(String[] args) throws Exception {
        String t1 = "t1";
        String t2 = "t2";
        String cf = "cf";
        if (args.length >= 3) {
            t1 = args[0];
            t2 = args[1];
            cf = args[2];
        }

        Configuration configuration = HBaseConfiguration.create();
        Scan scan = new Scan();
        scan.setCaching(500); // 1 is the default in Scan, which will be bad for MR
        scan.setCacheBlocks(false);

        HTable table1 = new HTable(configuration, t1);
        HTable table2 = new HTable(configuration, t2);
        ResultScanner r1 = table1.getScanner(scan);
        ResultScanner r2 = table2.getScanner(scan);

        try {
            int count = 0;
            compare:
            while (true) {
                Result ra = r1.next();
                Result rb = r2.next();
                count++;
                if ((count % (64 * 1024)) == 0) {
                    System.err.println("count = " + count);
                }
                if (ra == null && rb == null) {
                    System.err.println("Congratulations! They are same!");
                    break;
                } else if (ra == null) {
                    System.err.println("BAD! table '" + t2 + "' has more");
                    break;
                } else if (rb == null) {
                    System.err.println("BAD! table '" + t1 + "' has more");
                    break;
                } else {
                    if (!Arrays.equals(ra.getRow(), rb.getRow())) {
                        System.err.println("BAD! table '" + t1 + "' row '" + Bytes.toString(ra.getRow()) +
                                "', table '" + t2 + "' row '" + Bytes.toString(rb.getRow()) + "'");
                        break;
                    }
                    // damn.
                    NavigableMap<byte[], byte[]> d1 = ra.getNoVersionMap().get(cf.getBytes());
                    NavigableMap<byte[], byte[]> d2 = ra.getNoVersionMap().get(cf.getBytes());
                    Iterator<Map.Entry<byte[], byte[]>> iterator1 = d1.entrySet().iterator();
                    Iterator<Map.Entry<byte[], byte[]>> iterator2 = d2.entrySet().iterator();
                    while (iterator1.hasNext() && iterator2.hasNext()) {
                        Map.Entry<byte[], byte[]> i1 = iterator1.next();
                        Map.Entry<byte[], byte[]> i2 = iterator2.next();
                        byte[] k1 = i1.getKey();
                        byte[] v1 = i1.getValue();
                        byte[] k2 = i2.getKey();
                        byte[] v2 = i2.getValue();
                        if (!Arrays.equals(k1, k2)) {
                            System.err.println("BAD! table '" + t1 + "' row '" + Bytes.toString(ra.getRow()) + "' key '" + Bytes.toString(k1) + "', table '" +
                                    t2 + "' row '" + Bytes.toString(rb.getRow()) + "' key '" + Bytes.toString(k2) + "'");
                            break compare;
                        } else if (!Arrays.equals(v1, v2)) {
                            System.err.println("BAD! table '" + t1 + "' row '" + Bytes.toString(ra.getRow()) + "' key '" + Bytes.toString(k1) + "' value '" +
                                    Bytes.toString(v1) + ", table '" + t2 + "' row '" + Bytes.toString(rb.getRow()) + "' key '" + Bytes.toString(k2) +
                                    "' value '" + Bytes.toString(v2) + "'");

                            break compare;
                        }
                    }
                    if (iterator1.hasNext()) {
                        System.err.println("BAD! table '" + t1 + "' row '" + Bytes.toString(ra.getRow()) + "' has more");
                        break;
                    } else if (iterator2.hasNext()) {
                        System.err.println("BAD! table '" + t2 + "' row '" + Bytes.toString(rb.getRow()) + "' has more");
                        break;
                    }
                }
            }
        } finally {
            r1.close();
            r2.close();
            table1.close();
            table2.close();
        }
    }
}
