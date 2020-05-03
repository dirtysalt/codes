package com.dirlt.java.hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.util.Bytes;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 6/18/13
 * Time: 4:25 PM
 * To change this template use File | Settings | File Templates.
 */
public class RegionPreSplitting {
    public static void main(String[] args) throws Exception {
        // we have to insert data.
        Configuration configuration = HBaseConfiguration.create();
        HTable table = new HTable(configuration, "test");
        for (int i = 0; i < 10; i++) {
            Put put = new Put(Bytes.toBytes("row" + i));
            put.add(Bytes.toBytes("cf"),
                    Bytes.toBytes("__split_point"),
                    Bytes.toBytes("0"));
            table.put(put);
        }
        HBaseAdmin admin = new HBaseAdmin(HBaseConfiguration.create());
        for (int i = 1; i < 10; i += 1) {
            int count = table.getRegionsInfo().size();
            table.getRegionsInfo();
            admin.split(Bytes.toBytes("test"), Bytes.toBytes("row" + i));
            // since split is async operation, we have to wait.
            while (table.getRegionsInfo().size() == count) {
                Thread.sleep(1000);
            }
        }
    }
}
