package com.dirlt.java.mr;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 3/28/13
 * Time: 12:10 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestRenameOnExistPath {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        FileSystem fs = FileSystem.get(configuration);
        // NOTE(dirlt): notice if b is not empty directory
        // then rename will move a under b instead of changing name.
        fs.rename(new Path("/tmp/a"), new Path("/tmp/b"));
        fs.close();
    }
}
