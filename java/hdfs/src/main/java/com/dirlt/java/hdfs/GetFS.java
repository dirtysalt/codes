package com.dirlt.java.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

import java.net.URI;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/24/12
 * Time: 11:08 AM
 * To change this template use File | Settings | File Templates.
 */
public class GetFS {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        System.out.printf("fs.default.name = %s\n", configuration.get("fs.default.name"));

        FileSystem fs = FileSystem.get(configuration);
        System.out.printf("uri = %s\n", fs.getUri().toString());
        fs.close();

        FileSystem fs2 = FileSystem.get(new URI("file:///"), configuration);
        System.out.printf("uri = %s\n", fs2.getUri().toString());
        fs2.close();
    }
}
