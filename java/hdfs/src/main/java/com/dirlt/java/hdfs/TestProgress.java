package com.dirlt.java.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.util.Progressable;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/24/12
 * Time: 2:15 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestProgress {
    public static void main(String[] args) throws Exception {
        FileSystem fs = FileSystem.get(new Configuration());
        FSDataOutputStream writer = fs.create(new Path("/tmp/test"), true, 4096, new Progressable() {
            private int step = 0;

            @Override
            public void progress() {
                System.out.printf("step#%02d .....\n", step);
                step++;
            }
        });
        int count = 4;
        byte[] bs = new byte[32 * 1024];
        for (int i = 0; i < count; i++) {
            writer.write(bs);
        }
        writer.close();
        fs.close();
    }
}
