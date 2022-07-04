package com.starrocks.tools;

import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.GetObjectRequest;
import com.aliyun.oss.model.OSSObject;
import com.aliyun.oss.model.OSSObjectSummary;
import com.aliyun.oss.model.ObjectListing;
import com.aliyun.oss.model.SimplifiedObjectMeta;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class MyOSSClient implements ObjectClient {
    private OSS client;

    private MyOSSClient(OSS client) {
        this.client = client;
    }

    public byte[] readObject(String bucket, String objectKey, long offset, long size) throws IOException {
        GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, objectKey);
        getObjectRequest.setRange(offset, offset + size - 1);
        OSSObject ossObject = client.getObject(getObjectRequest);
        InputStream in = ossObject.getObjectContent();
        byte[] data = new byte[(int) size];
        int read = 0;
        while (true) {
            int n = in.read(data, read, data.length);
            if (n == -1) {
                break;
            }
            read += n;
        }
        if (read != size) {
            System.out.println(
                    String.format("Read failed. expected size = %d, actual size = %d", size, read));
            return null;
        }

        return data;
    }

    public void listObjects(String bucket, String path, List<ObjectMeta> objectMetaList)
            throws IOException {
        ObjectListing list = client.listObjects(bucket, path);
        for (OSSObjectSummary obj : list.getObjectSummaries()) {
            if (obj.getSize() == 0) {
                continue;
            }
            ObjectMeta objectMeta = new ObjectMeta();
            objectMeta.name = obj.getKey();
            objectMeta.size = obj.getSize();
            objectMetaList.add(objectMeta);
        }
    }

    public void headObject(String bucket, String objectKey, List<ObjectMeta> objectMetaList)
            throws IOException {
        SimplifiedObjectMeta meta = client.getSimplifiedObjectMeta(bucket, objectKey);
        // What if not existed ??
        if (meta.getSize() > 0) {
            ObjectMeta objectMeta = new ObjectMeta();
            objectMeta.name = objectKey;
            objectMeta.size = meta.getSize();
            objectMetaList.add(objectMeta);
        }
    }

    public static ObjectClient build(String endpoint, String cred) {
        String[] parts = cred.split(":");
        String accessKey = parts[0];
        String secretKey = parts[1];
        OSS oss = new OSSClientBuilder().build(endpoint, accessKey, secretKey);
        return new MyOSSClient(oss);
    }
}
