package com.dirlt.java.hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/20/12
 * Time: 12:09 PM
 * To change this template use File | Settings | File Templates.
 */
public class MaxPutSize {
    private final static String kTableName = "t1";
    private final static byte[] kByteColumnFamily = Bytes.toBytes("cf");
    private final static byte[] kByteColumn = Bytes.toBytes("cl");
    private static Configuration configuration = HBaseConfiguration.create();

    public static void run() throws IOException {
        // prepare table.
        HBaseAdmin admin = new HBaseAdmin(configuration);
        if (admin.tableExists(kTableName)) {
            admin.disableTable(kTableName);
            admin.deleteTable(kTableName);
        }
        HTableDescriptor dp = new HTableDescriptor(kTableName);
        dp.addFamily(new HColumnDescriptor(kByteColumnFamily));
        admin.createTable(dp);

        HTable table = new HTable(kTableName);
        // starts with.
        int size = 2048;
        while (true) {
            byte[] value = new byte[size - 1];
            Put put = new Put(Bytes.toBytes("row"));
            put.add(kByteColumnFamily, kByteColumn, value);
            try {
                table.put(put);
            } catch (IllegalArgumentException e) {
                e.printStackTrace();
                break;
            }
            System.out.println("value size = " + size + ", succeed");
            if (size >= 8 * 1024 * 1024) {
                break;
            }
            size *= 2;
        }
        table.close();
        admin.disableTable(kTableName);
        admin.deleteTable(kTableName);
    }

    public static void main(String[] args) throws IOException {
        Configuration conf = HBaseConfiguration.create();
        MaxPutSize test = new MaxPutSize();
        test.run();
    }
}