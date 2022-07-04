package com.starrocks.tools;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.core.ResponseBytes;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3ClientBuilder;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.HeadObjectRequest;
import software.amazon.awssdk.services.s3.model.HeadObjectResponse;
import software.amazon.awssdk.services.s3.model.ListObjectsRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsResponse;
import software.amazon.awssdk.services.s3.model.NoSuchKeyException;
import software.amazon.awssdk.services.s3.model.S3Object;

import java.io.IOException;
import java.net.URI;
import java.util.List;

public class MyS3Client implements ObjectClient {
    private S3Client client;

    private MyS3Client(S3Client client) {
        this.client = client;
    }

    public byte[] readObject(String bucket, String objectKey, long offset, long size) throws IOException {
        String range = String.format("bytes=%d-%d\n", offset, offset + size - 1);
        GetObjectRequest objectRequest = GetObjectRequest
                .builder()
                .key(objectKey)
                .bucket(bucket)
                .range(range)
                .build();
        ResponseBytes<GetObjectResponse> objectBytes = client.getObjectAsBytes(objectRequest);
        byte[] data = objectBytes.asByteArray();
        if (data.length != size) {
            System.out.println(
                    String.format("Read failed. expected size = %d, actual size = %d", size, data.length));
            return null;
        }
        return data;
    }

    public void listObjects(String bucket, String path, List<ObjectMeta> objectMetaList)
            throws IOException {
        ListObjectsRequest listObjectsRequest =
                ListObjectsRequest.builder().bucket(bucket).prefix(path).build();
        ListObjectsResponse listObjectsResponse = client.listObjects(listObjectsRequest);
        for (S3Object obj : listObjectsResponse.contents()) {
            if (obj.size() == 0) {
                continue;
            }
            ObjectMeta objectMeta = new ObjectMeta();
            objectMeta.name = obj.key();
            objectMeta.size = obj.size();
            objectMetaList.add(objectMeta);
        }
    }

    public void headObject(String bucket, String objectKey, List<ObjectMeta> objectMetaList)
            throws IOException {
        HeadObjectRequest objectRequest = HeadObjectRequest
                .builder()
                .key(objectKey)
                .bucket(bucket)
                .build();
        long size = 0;
        try {
            HeadObjectResponse resp = client.headObject(objectRequest);
            size = resp.contentLength();
        } catch (NoSuchKeyException e) {
            return;
        }
        if (size == 0) {
            return;
        }
        ObjectMeta objectMeta = new ObjectMeta();
        objectMeta.name = objectKey;
        objectMeta.size = size;
        objectMetaList.add(objectMeta);
    }

    public static ObjectClient build(String endpoint, String cred) {
        URI uri = URI.create(endpoint);
        S3ClientBuilder builder = S3Client.builder().endpointOverride(uri);
        if (cred != null) {
            String[] parts = cred.split(":");
            String accessKey = parts[0];
            String secretKey = parts[1];
            AwsCredentialsProvider credentialsProvider =
                    StaticCredentialsProvider.create(AwsBasicCredentials.create(accessKey, secretKey));
            builder.credentialsProvider(credentialsProvider);
        }
        S3Client client = builder.build();
        return new MyS3Client(client);
    }
}
