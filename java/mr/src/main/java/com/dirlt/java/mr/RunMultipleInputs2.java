package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapper;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

// multiple table and multiple file
public class RunMultipleInputs2 {
    public static final String CLASS_NAME = RunMultipleInputs2.class.getSimpleName();
    public static final String kInTableName1 = "t1";
    public static final String kInTableName2 = "t2";
    public static final String kInFileName1 = "/tmp/in1";
    public static final String kInFileName2 = "/tmp/in2";
    public static final String kOutFileName = "/tmp/tout";
    private final static byte[] kByteColumnFamily = Bytes.toBytes("cf");
    private final static byte[] kByteColumn = Bytes.toBytes("cl");

    public static class FMapper extends Mapper<LongWritable, Text, Text, Text> {
        @Override
        protected void map(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
            context.write(new Text("0"),
                    new Text("file mapper value=" + value.toString()));
        }
    }

    public static class TMapper extends TableMapper<Text, Text> {
        @Override
        protected void map(ImmutableBytesWritable key, Result result,
                           Context context) throws IOException, InterruptedException {
            context.write(
                    new Text("0"),
                    new Text("table mapper key = "
                            + Bytes.toString(key.get())
                            + ", value="
                            + Bytes.toString(result.getValue(kByteColumnFamily,
                            kByteColumn))));
        }
    }


    public static class _Reducer extends
            Reducer<Text, Text, NullWritable, Text> {
        @Override
        protected void reduce(Text key, Iterable<Text> values, Context context)
                throws IOException, InterruptedException {
            for (Text v : values) {
                context.write(null, v);
            }
        }
    }

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

        HTable table = new HTable(name);
        Put put = new Put(Bytes.toBytes(name + ".fk"));
        put.add(kByteColumnFamily, kByteColumn, Bytes.toBytes(name + ".value"));
        table.put(put);
        table.close();
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

    public static Job configureJob(Configuration conf, String[] args)
            throws IOException {
        createTable(kInTableName1, conf);
        createTable(kInTableName2, conf);
        createFile(kInFileName1, conf);
        createFile(kInFileName2, conf);
        deleteFile(kOutFileName, conf);

        String jobName = CLASS_NAME;
        // setup environment.
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(RunMultipleInputs2.class);

        // mapper option.
        Scan scan = new Scan();
        scan.setCaching(500);
        String tableInput1 = MultipleTableInputFormat.convertTableInputToString(kInTableName1, scan);
        String tableInput2 = MultipleTableInputFormat.convertTableInputToString(kInTableName2, scan);
        MultipleInputs.addInputPath(job, new Path(tableInput1), MultipleTableInputFormat.class, TMapper.class);
        MultipleInputs.addInputPath(job, new Path(tableInput2), MultipleTableInputFormat.class, TMapper.class);
        MultipleInputs.addInputPath(job, new Path(kInFileName1), TextInputFormat.class, FMapper.class);
        MultipleInputs.addInputPath(job, new Path(kInFileName2), TextInputFormat.class, FMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        // reducer option.
        job.setReducerClass(Reducer.class);
        job.setOutputKeyClass(NullWritable.class);
        job.setOutputValueClass(Text.class);
        job.setNumReduceTasks(1); // just one reducer.

        // output option.
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path(kOutFileName));
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