package com.starrocks.tools;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;

import java.io.IOException;
import java.net.URI;
import java.util.List;

public class MyHDFSClient implements ObjectClient {
    private final FileSystem fs;

    private MyHDFSClient(FileSystem fs) {
        this.fs = fs;
    }

    public byte[] readObject(String bucket, String objectKey, long offset, long size) throws IOException {
        // there is no bucket concept in HDFS.
        Path path = new Path(objectKey);
        FSDataInputStream inputStream = fs.open(path);
        int iSize = (int) size;
        byte[] data = new byte[iSize];
        int read = inputStream.read(offset, data, 0, iSize);
        if (read != iSize) {
            System.out.printf("Read failed. expected size = %d, actual size = %d%n", size, read);
            return null;
        }
        return data;
    }

    public void listObjects(String bucket, String path, List<ObjectMeta> objectMetaList)
            throws IOException {
        RemoteIterator<LocatedFileStatus> resp = fs.listFiles(new Path(path), false);
        while (resp.hasNext()) {
            LocatedFileStatus st = resp.next();

            String name = st.getPath().getName();
            long size = st.getLen();
            if (size == 0) {
                continue;
            }
            ObjectMeta objectMeta = new ObjectMeta();
            objectMeta.name = path + name;
            objectMeta.size = size;
            objectMetaList.add(objectMeta);
        }
    }

    public void headObject(String bucket, String objectKey, List<ObjectMeta> objectMetaList)
            throws IOException {
        FileStatus st = fs.getFileStatus(new Path(objectKey));
        if (st.getLen() == 0) {
            return;
        }
        ObjectMeta objectMeta = new ObjectMeta();
        objectMeta.name = objectKey;
        objectMeta.size = st.getLen();
        objectMetaList.add(objectMeta);
    }

    public static ObjectClient build(String endpoint) {
        Configuration conf = new Configuration();
        // Set FileSystem URI
        conf.set("fs.defaultFS", endpoint);
        // Because of Maven
        conf.set("fs.hdfs.impl", org.apache.hadoop.hdfs.DistributedFileSystem.class.getName());
        conf.set("fs.file.impl", org.apache.hadoop.fs.LocalFileSystem.class.getName());
        // Set HADOOP user
        //        System.setProperty("HADOOP_USER_NAME", "hdfs");
        //        System.setProperty("hadoop.home.dir", "/");

        try {
            FileSystem fs = FileSystem.get(URI.create(endpoint), conf);
            fs.setWorkingDirectory(new Path("/"));
            return new MyHDFSClient(fs);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
}
