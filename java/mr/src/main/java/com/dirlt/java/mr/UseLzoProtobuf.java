package com.dirlt.java.mr;

import com.dirlt.java.mr.proto.MessageProtos1;
import com.hadoop.compression.lzo.DistributedLzoIndexer;
import com.hadoop.compression.lzo.LzoIndexer;
import com.twitter.elephantbird.mapreduce.io.ProtobufWritable;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 7:33 PM
 * To change this template use File | Settings | File Templates.
 */
public class UseLzoProtobuf {
    public static final String kInputFileName = "/tmp/test/in";
    public static final String kOutputFileName = "/tmp/test/out";
    public static final String kOutputFileName2 = "/tmp/test/out2";

    public static final String CLASS_NAME = UseLzoProtobuf.class.getSimpleName();

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

    public static class Mapper1 extends Mapper<LongWritable, Text, NullWritable, MessageLzoProtobufWritable> {
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            MessageProtos1.Message.Builder builder = MessageProtos1.Message.newBuilder();
            builder.setText(value.toString());
            context.write(null, new MessageLzoProtobufWritable(builder.build()));
        }
    }

    public static class Mapper2 extends Mapper<LongWritable, ProtobufWritable<MessageProtos1.Message>, NullWritable, Text> {
        @Override
        public void map(LongWritable key, ProtobufWritable<MessageProtos1.Message> value, Context context) throws IOException, InterruptedException {
            value.setConverter(MessageProtos1.Message.class);
            MessageProtos1.Message message = value.get();
            System.out.println(message.getText());
            context.write(null, new Text(message.getText()));
        }
    }

    public static Job configureJob1(Configuration conf) throws IOException {
        createFile(kInputFileName, conf);
        deleteFile(kOutputFileName, conf);

        // setup environment.
        String jobName = CLASS_NAME;
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(UseLzoProtobuf.class);
        job.setMapperClass(Mapper1.class);
        job.setMapOutputKeyClass(NullWritable.class);
        job.setMapOutputValueClass(MessageLzoProtobufWritable.class);
        job.setInputFormatClass(TextInputFormat.class);
        FileInputFormat.setInputPaths(job, new Path(kInputFileName));
        job.setOutputFormatClass(MessageLzoProtobufOutputFormat.class);
        FileOutputFormat.setOutputPath(job, new Path(kOutputFileName));
        job.setNumReduceTasks(0);
        return job;
    }

    public static Job configureJob2(Configuration conf) throws IOException {
        deleteFile(kOutputFileName2, conf);

        // setup environment.
        String jobName = CLASS_NAME;
        Job job = new Job(conf);
        job.setJobName(jobName);
        job.setJarByClass(UseLzoProtobuf.class);
        job.setMapperClass(Mapper2.class);
        job.setMapOutputKeyClass(NullWritable.class);
        job.setMapOutputValueClass(Text.class);
        job.setInputFormatClass(MessageLzoProtobufInputFormat.class);
        FileInputFormat.setInputPaths(job, new Path(kOutputFileName));
        job.setOutputFormatClass(TextOutputFormat.class);
        FileOutputFormat.setOutputPath(job, new Path(kOutputFileName2));
        job.setNumReduceTasks(0);
        return job;
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        conf.set("io.compression.codecs", "org.apache.hadoop.io.compress.DefaultCodec,org.apache.hadoop.io.compress.GzipCodec,com.hadoop.compression.lzo.LzopCodec");
        conf.set("io.compression.codec.lzo.class", "com.hadoop.compression.lzo.LzoCodec");
        args = new GenericOptionsParser(conf, args).getRemainingArgs();
        Job job = configureJob1(conf);
        job.submit();
        job.waitForCompletion(true);

        // make index.
        LzoIndexer.main(new String[]{kOutputFileName});

        job = configureJob2(conf);
        job.submit();
        job.waitForCompletion(true);
    }
}
