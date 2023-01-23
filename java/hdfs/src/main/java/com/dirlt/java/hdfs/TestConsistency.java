package com.dirlt.java.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/24/12
 * Time: 11:53 AM
 * To change this template use File | Settings | File Templates.
 */
public class TestConsistency {
    public static void withoutSync() throws Exception {
        // assure it's hdfs.
        FileSystem fs = FileSystem.get(new Configuration());
        System.out.println("uri = " + fs.getUri().toString());
        Path path = new Path("/tmp/test");

        FSDataOutputStream writer = fs.create(path, true);
        writer.write("hello".getBytes());

        writer.flush();
        System.out.printf("after flush length = %d\n", (int) fs.getFileStatus(path).getLen());

        writer.sync();
        writer.sync();
        System.out.printf("after sync length = %d\n", (int) fs.getFileStatus(path).getLen());

        writer.close();
        System.out.printf("after close length = %d\n", (int) fs.getFileStatus(path).getLen());
        fs.close();
    }

    public static void main(String[] args) throws Exception {
        withoutSync();
    }
}
