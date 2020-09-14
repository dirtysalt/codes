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
import org.apache.hadoop.hbase.mapreduce.MultiTableOutputFormat;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

public class RunMultipleOutputs {
    public static final String CLASS_NAME = RunMultipleOutputs.class.getSimpleName();
    public static final String kInputFileName = "/tmp/test/in";
    public static final String kOutputTableName = "t1";
    public static final String kOutputTableName2 = "t2";
    public static final String kOutputFileName = "/tmp/test/out";
    public static final String kOutputFileDir2 = "/tmp/test2/";
    public static final String kOutputFileName2 = "/tmp/test2/out";
    public static final String kOutputPrefix = "out.prefix";
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

    public static class _Mapper extends Mapper<LongWritable, Text, NullWritable, NullWritable> {
        private MultipleOutputsInterface mos = null;

        @Override
        public void setup(Context ctx) throws IOException, InterruptedException {
            super.setup(ctx);
            if (mos == null) {
                mos = new DefaultMultipleOutput(ctx);
            }
        }

        public void setMultipleOutputs(MultipleOutputsInterface mos) {
            this.mos = mos;
        }

        @Override
        public void map(LongWritable k, Text v, Context ctx) throws IOException, InterruptedException {
            mos.write("f", new Text("fk"), v); // test/out/f-m-00000
            mos.write("f2", new Text("fk"), v); // test/out/f2-m-00000
            mos.write("f3", new Text("fk"), v, kOutputFileName2); // test2/out-m-00000
            // a little weird.
            mos.write("f3", new Text("fk"), v, kOutputPrefix); // test/out/out.prefix-m-00000
            Put put = new Put(Bytes.toBytes("tk"));
            put.add(kByteColumnFamily, kByteColumn, v.getBytes());
            mos.write("t", new ImmutableBytesWritable(Bytes.toBytes(kOutputTableName)), put);
            mos.write("t2", new ImmutableBytesWritable(Bytes.toBytes(kOutputTableName2)), put);
        }

        @Override
        public void cleanup(Context ctx) throws IOException, InterruptedException {
            super.cleanup(ctx);
            mos.close();
        }
    }

    public static Job configureJob(Configuration conf, String[] args)
            throws IOException {
        createTable(kOutputTableName, conf);
        createTable(kOutputTableName2, conf);
        deleteFile(kOutputFileName, conf);
        deleteFile(kOutputFileDir2, conf);
        createFile(kInputFileName, conf);

        String jobName = CLASS_NAME;
        // setup environment.
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(RunMultipleOutputs.class);
        job.setMapperClass(_Mapper.class);
        FileInputFormat.setInputPaths(job, new Path(kInputFileName));

        MultipleOutputs.addNamedOutput(job, "f", TextOutputFormat.class, Text.class, Text.class);
        MultipleOutputs.addNamedOutput(job, "f2", TextOutputFormat.class, Text.class, Text.class);
        MultipleOutputs.addNamedOutput(job, "f3", TextOutputFormat.class, Text.class, Text.class);
        MultipleOutputs.addNamedOutput(job, "t", MultiTableOutputFormat.class, ImmutableBytesWritable.class, Put.class);
        MultipleOutputs.addNamedOutput(job, "t2", MultiTableOutputFormat.class, ImmutableBytesWritable.class, Put.class);
        FileOutputFormat.setOutputPath(job, new Path(kOutputFileName));

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
