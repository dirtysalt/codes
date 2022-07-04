package com.starrocks.tools;

import java.io.IOException;
import java.util.List;

public interface ObjectClient {
    public static class ObjectMeta {
        public String name;
        public long size;
    }

    public byte[] readObject(String bucket, String objectKey, long offset, long size) throws IOException;

    public void listObjects(String bucket, String path, List<ObjectMeta> objectMetaList) throws IOException;

    public void headObject(String bucket, String objectKey, List<ObjectMeta> objectMetaList)
            throws IOException;
}
