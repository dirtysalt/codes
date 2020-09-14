package com.dirlt.java.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FsStatus;
import org.apache.hadoop.hdfs.DFSClient;
import org.apache.hadoop.hdfs.protocol.DatanodeInfo;
import org.apache.hadoop.hdfs.protocol.FSConstants;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 5/8/13
 * Time: 1:55 PM
 * To change this template use File | Settings | File Templates.
 */
public class ClusterSummary {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        DFSClient client = new DFSClient(configuration);

        System.out.println("missing block=" + client.getMissingBlocksCount() + ", corrupt block=" + client.getCorruptBlocksCount() +
                ", under-replicated block=" + client.getUnderReplicatedBlocksCount());
        System.out.println("default block size=" + client.getDefaultBlockSize() + ", default replication number=" + client.getDefaultReplication());
        FsStatus fsStatus = client.getDiskStatus();
        System.out.println("dfs total=" + fsStatus.getCapacity() + ", dfs used=" + fsStatus.getUsed() +
                ", dfs remaining=" + fsStatus.getRemaining());
        DatanodeInfo infos[] = client.datanodeReport(FSConstants.DatanodeReportType.ALL); // LIVE OR DEAD.
        for (DatanodeInfo info : infos) {
            System.out.println("node=" + info.getHostName() + ", remaining percent=" + info.getRemainingPercent());
        }
    }
}