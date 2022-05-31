package com.dirlt.java.jni;

import java.io.File;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.StandardOpenOption;

public class SMOnFileChannel {
    public static void main(String[] args) throws IOException, InterruptedException {
        File f = new File("/tmp/test-file-channel.txt");
        FileChannel fc = FileChannel.open(f.toPath(), StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING,
                StandardOpenOption.READ,
                StandardOpenOption.WRITE);
        MappedByteBuffer b = fc.map(FileChannel.MapMode.READ_WRITE, 0, 4096);
        String data = "hello, world\0";
        b.put(data.getBytes());
        System.out.println("Write down. Waiting client");

        while (b.get(0) != '!') {
            Thread.sleep(1000);
        }
        System.out.println("OK. quit");
        f.delete();
    }
}
