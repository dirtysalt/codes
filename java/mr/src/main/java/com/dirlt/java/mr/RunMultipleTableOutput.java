package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapred.TableOutputFormat;
import org.apache.hadoop.hbase.mapreduce.MultiTableOutputFormat;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

public class RunMultipleTableOutput {
    public static final String CLASS_NAME = RunMultipleTableOutput.class.getSimpleName();

    public static final String kInputFileName = "/tmp/test/in";
    public static final String kOutputTableName = "t1";
    public static final String kOutputTableName2 = "t2";
    private final static byte[] kByteColumnFamily = Bytes.toBytes("cf");
    private final static byte[] kByteColumn = Bytes.toBytes("cl");

    public static void createTable(String name, Configuration conf)
            throws IOException {
        HBaseAdmin admin = new HBaseAdmin(conf);
        if (admin.isTableAvailable(name)) {
            admin.disableTable(name);
            admin.deleteTable(name);
        }
        HTableDescriptor dp = new HTableDescriptor(name);
        dp.addFamily(new HColumnDescriptor(kByteColumnFamily));
        admin.createTable(dp);
    }

    public static void createFile(String name, Configuration conf)
            throws IOException {
        FileSystem fs = FileSystem.get(conf);
        Path p = new Path(name);
        if (fs.exists(p)) {
            fs.delete(p, true);
        }
        FSDataOutputStream fos = fs.create(p);
        fos.writeBytes(name + ".value\n");
        fos.close();
        fs.close();
    }

    public static void deleteFile(String name, Configuration conf)
            throws IOException {
        FileSystem fs = FileSystem.get(conf);
        Path p = new Path(name);
        if (fs.exists(p)) {
            fs.delete(p, true);
        }
        fs.close();
    }

    public static class _Mapper extends Mapper<LongWritable, Text, ImmutableBytesWritable, Put> {
        @Override
        public void map(LongWritable k, Text v, Context ctx) throws IOException, InterruptedException {
            Put put = new Put(Bytes.toBytes("tk"));
            put.add(kByteColumnFamily, kByteColumn, v.getBytes());
            ctx.write(new ImmutableBytesWritable(Bytes.toBytes(kOutputTableName)), put);
            ctx.write(new ImmutableBytesWritable(Bytes.toBytes(kOutputTableName2)), put);
        }
    }

    public static Job configureJob(Configuration conf, String[] args)
            throws IOException {
        createTable(kOutputTableName, conf);
        createTable(kOutputTableName2, conf);
        createFile(kInputFileName, conf);

        // setup environment.
        String jobName = CLASS_NAME;
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(RunMultipleTableOutput.class);
        job.setMapperClass(_Mapper.class);
        FileInputFormat.setInputPaths(job, new Path(kInputFileName));
        job.setOutputFormatClass(MultiTableOutputFormat.class);
        job.setNumReduceTasks(0);
        return job;
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = HBaseConfiguration.create();
        args = new GenericOptionsParser(conf, args).getRemainingArgs();
        Job job = configureJob(conf, args);
        job.submit();
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}