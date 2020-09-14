package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.HFileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

// assume hdfs sequence file input format
// key is immutable bytes, value is put(writable)
// specify hbase table name and column family by parameters.

public class HBaseLoaderMR {
    public static final String CLASS_NAME = HBaseLoaderMR.class.getSimpleName();

    public static class IdentityMapper extends Mapper<ImmutableBytesWritable, Put, ImmutableBytesWritable, Put> {
        public void map(ImmutableBytesWritable key, Put value, Context context) throws IOException, InterruptedException {
            context.write(key, value);
        }
    }

    public static Job configureJob(Configuration configuration, String[] args) throws IOException {
        String tableName = null;
        String inputPath = null;
        String outputPath = null;
        for (String arg : args) {
            if (arg.startsWith("--table=")) {
                tableName = arg.substring("--table=".length());
            } else if (arg.startsWith("--input=")) {
                inputPath = arg.substring("--input=".length());
            } else if (arg.startsWith("--output=")) {
                outputPath = arg.substring("--output=".length());
            }
        }

        String jobName = CLASS_NAME + "#" + inputPath;
        Job job = new Job(configuration, jobName);
        job.setJarByClass(HBaseLoaderMR.class);

        // mapper.
        job.setMapperClass(IdentityMapper.class);
        job.setMapOutputKeyClass(ImmutableBytesWritable.class);
        job.setMapOutputValueClass(Put.class);
        job.setNumReduceTasks(0);

        // input and output option.
        // read in text in lzo format.
        job.setInputFormatClass(SequenceFileInputFormat.class);
        job.setOutputFormatClass(HFileOutputFormat.class);
        SequenceFileInputFormat.addInputPaths(job, inputPath);
        HFileOutputFormat.setOutputPath(job, new Path(outputPath));

        HTable table = new HTable(configuration, tableName);
        // change reduce class.
        HFileOutputFormat.configureIncrementalLoad(job, table);
        return job;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = HBaseConfiguration.create();
        args = new GenericOptionsParser(configuration, args).getRemainingArgs();
        Job job = configureJob(configuration, args);
        job.submit();
        job.waitForCompletion(true);
    }
}
