package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

import java.io.IOException;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 4/9/13
 * Time: 12:54 PM
 * To change this template use File | Settings | File Templates.
 */
public class DeleteFile {
    public static void main(String[] args) throws IOException {
        Configuration configuration = new Configuration();
        FileSystem fileSystem = FileSystem.get(configuration);
        fileSystem.delete(new Path("/tmp/delete-file"), true);
        fileSystem.close();
    }
}
