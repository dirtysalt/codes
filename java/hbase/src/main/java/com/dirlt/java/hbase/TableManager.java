package com.dirlt.java.hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.IOException;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/20/12
 * Time: 10:46 AM
 * To change this template use File | Settings | File Templates.
 */
public class TableManager {
    private static Configuration configuration = HBaseConfiguration.create();
    private static final String kTableName = "t1";
    private static final String kColumnFamily = "cf";
    private static HBaseAdmin admin;

    static {
        try {
            admin = new HBaseAdmin(configuration);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void createTable() throws IOException {
        HTableDescriptor desc = new HTableDescriptor(kTableName);
        desc.addFamily(new HColumnDescriptor(Bytes.toBytes(kColumnFamily)));
        admin.createTable(desc);
    }

    public static void deleteTable() throws IOException {
        if (admin.tableExists(kTableName)) {
            if (admin.isTableEnabled(kTableName)) {
                admin.disableTable(kTableName);
            }
            admin.deleteTable(kTableName);
        }
    }

    public static void main(String[] args) throws IOException {
        deleteTable();
        createTable();
    }
}
