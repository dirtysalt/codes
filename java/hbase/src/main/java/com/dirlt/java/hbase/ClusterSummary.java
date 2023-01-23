package com.dirlt.java.hbase;

import org.apache.hadoop.hbase.ClusterStatus;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HServerInfo;
import org.apache.hadoop.hbase.HServerLoad;
import org.apache.hadoop.hbase.client.HBaseAdmin;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 5/8/13
 * Time: 2:32 PM
 * To change this template use File | Settings | File Templates.
 */
public class ClusterSummary {
    public static void main(String[] args) throws Exception {
        HBaseAdmin admin = new HBaseAdmin(HBaseConfiguration.create());
        ClusterStatus clusterStatus = admin.getClusterStatus();
        System.out.println("request count=" + clusterStatus.getRequestsCount() + ", region count=" + clusterStatus.getRegionsCount());
        for (HServerInfo info : clusterStatus.getServerInfo()) {
            HServerLoad load = info.getLoad();
            System.out.println("node=" + info.getHostname() + ", load=" + load.getLoad());
        }
    }
}
