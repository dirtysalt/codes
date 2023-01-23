package com.dirlt.java.mr;

import org.apache.hadoop.mapred.ClusterStatus;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.JobStatus;

import java.io.IOException;

public class ClusterSummary {
    public static void main(String[] args) throws IOException {
        JobConf jobConf = new JobConf();
        JobClient jobClient = new JobClient(jobConf);
        JobStatus[] jobStatuses = jobClient.getAllJobs();
        for (JobStatus jobStatus : jobStatuses) {
            System.out.println("id=" + jobStatus.getJobID().toString() + ",setup="
                    + jobStatus.setupProgress() + ",cleanup=" + jobStatus.cleanupProgress()
                    + ",map=" + jobStatus.mapProgress() + ",reduce="
                    + jobStatus.reduceProgress() + ",status="
                    + JobStatus.getJobRunState(jobStatus.getRunState()));
        }
        ClusterStatus cs = jobClient.getClusterStatus(true);
        System.out.println("map-capacity=" + cs.getMaxMapTasks() + ",map-used="
                + cs.getMapTasks() + ",reduce-capacity=" + cs.getMaxReduceTasks()
                + ",reduce-used=" + cs.getReduceTasks());
        // TODO(dirlt): much more information.
        System.out.println("JT: max-memory=" + cs.getMaxMemory() + ", used-memory=" + cs.getUsedMemory());
        System.out.println("excluded: " + cs.getNumExcludedNodes() + " hosts");
        System.out.println("active hosts:");
        for (String host : cs.getActiveTrackerNames()) {
            System.out.println("\t" + host);
        }
        System.out.println("blacklisted hosts:");
        for (String host : cs.getBlacklistedTrackerNames()) {
            System.out.println("\t" + host);
        }
    }
}
