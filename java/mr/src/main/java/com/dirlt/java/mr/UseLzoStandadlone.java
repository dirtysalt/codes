package com.dirlt.java.mr;

import com.hadoop.compression.lzo.LzopCodec;
import org.apache.hadoop.conf.Configuration;

import java.io.*;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 2/18/13
 * Time: 11:49 AM
 * To change this template use File | Settings | File Templates.
 */
public class UseLzoStandadlone {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        // whether to use native implementation.
        configuration.setBoolean("hadoop.native.lib", true);
        configuration.set("io.compression.codec.lzo.compressor","LZO1X_1");
        configuration.setInt("io.compression.codec.lzo.compression.level", 5);
        configuration.setInt("io.compression.codec.lzo.buffersize", 256 * 1024);
        LzopCodec codec = new LzopCodec();
        codec.setConf(configuration);

        FileOutputStream fos = new FileOutputStream("/tmp/test.lzo");
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(codec.createOutputStream(fos)));
        writer.write("hello,world");
        writer.newLine();
        writer.close();
        fos.close();

        FileInputStream fis = new FileInputStream("/tmp/test.lzo");
        BufferedReader reader = new BufferedReader(new InputStreamReader(codec.createInputStream(fis)));
        String s = reader.readLine();
        System.out.println(s);
        reader.close();
        fis.close();
    }
}
