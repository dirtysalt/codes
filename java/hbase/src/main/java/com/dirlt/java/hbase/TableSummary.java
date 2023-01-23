package com.dirlt.java.hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HRegionInfo;
import org.apache.hadoop.hbase.HServerAddress;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.util.Bytes;

import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 6/19/13
 * Time: 10:52 AM
 * To change this template use File | Settings | File Templates.
 */
public class TableSummary {
    public static void main(String[] args) throws Exception {
        Configuration configuration = HBaseConfiguration.create();

        String tableName = "test";
        for (String arg : args) {
            if (arg.startsWith("--table=")) {
                tableName = arg.substring("--table=".length());
            }
        }

        HTable table = new HTable(configuration, tableName);
        Map<HRegionInfo, HServerAddress> dist = table.getRegionsInfo();
        for (HRegionInfo info : dist.keySet()) {
            System.out.printf("id = %s, name = %s, startKey = %s, endKey = %s\n", "" + info.getRegionId(), info.getRegionNameAsString(),
                    Bytes.toString(info.getStartKey()), Bytes.toString(info.getEndKey()));
        }
    }
}
