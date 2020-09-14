package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import java.io.IOException;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/27/12
 * Time: 12:13 PM
 * To change this template use File | Settings | File Templates.
 */
public class ReadGZipInput {
    public static final String CLASS_NAME = ReadGZipInput.class.getSimpleName();
    private static final String kInputFileName = ReadGZipInput.class.getResource("/gz").getPath();
    private static final String kOutputFileName = "/tmp/out";

    public static class _Mapper extends Mapper<LongWritable, Text, NullWritable, NullWritable> {
        @Override
        public void map(LongWritable key, Text value, Context context) {
            System.out.println(value.toString());
        }
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
        deleteFile(kOutputFileName, conf);

        String jobName = CLASS_NAME;
        // setup environment.
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(ReadGZipInput.class);

        // mapper option.
        job.setMapperClass(_Mapper.class);
        job.setMapOutputKeyClass(NullWritable.class);
        job.setMapOutputValueClass(NullWritable.class);

        // reducer option.
        job.setNumReduceTasks(0); // just one reducer.

        // input option.
        job.setInputFormatClass(TextInputFormat.class);
        FileInputFormat.setInputPaths(job, kInputFileName);

        // output option.
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path(kOutputFileName));
        return job;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        Job job = configureJob(configuration, args);
        job.submit();
        job.waitForCompletion(true);
    }
}
