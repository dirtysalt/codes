package com.starrocks.javaproxy;

import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import com.google.common.cache.RemovalListener;
import com.google.common.cache.RemovalNotification;
import com.google.protobuf.ByteString;
import io.grpc.stub.StreamObserver;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hdfs.DFSInputStream;
import org.apache.hadoop.hdfs.client.HdfsDataInputStream;

import java.io.IOException;
import java.net.URI;
import java.nio.ByteBuffer;
import java.time.Duration;
import java.util.UUID;

public class HdfsRpcHandler extends PInternalServiceGrpc.PInternalServiceImplBase {
    private static class CacheValue {
        public FileSystem fs;
        public Path path;
        public FSDataInputStream inputStream;
        public ByteBuffer buffer;
    }

    private Configuration configuration;
    private Cache<String, CacheValue> cache;

    public HdfsRpcHandler() {
        Configuration conf = new Configuration();
        conf.set("fs.hdfs.impl", org.apache.hadoop.hdfs.DistributedFileSystem.class.getName());
        conf.set("fs.file.impl", org.apache.hadoop.fs.LocalFileSystem.class.getName());
        configuration = conf;

        cache = CacheBuilder.newBuilder()
                .expireAfterAccess(Duration.ofMinutes(5))
                .removalListener(new RemovalListener<String, CacheValue>() {
                    @Override
                    public void onRemoval(RemovalNotification<String, CacheValue> notification) {
                        CacheValue cv = notification.getValue();
                        System.out.printf("release sssion %s\n", notification.getKey());
                        cv.buffer.clear();
                        try {
                            cv.inputStream.close();
                        } catch (IOException e) {
                        }
                        try {
                            cv.fs.close();
                        } catch (IOException e) {
                        }

                    }
                })
                .build();
    }

    // ============================================================
    private ByteBuffer newBuffer(int size) {
        int cap = 1024;
        while (cap < size) {
            cap *= 2;
        }
        return ByteBuffer.allocate(cap);
    }

    private ByteBuffer resizeBuffer(ByteBuffer buffer, int size) {
        int cap = buffer.capacity();
        if (cap >= size) {
            return buffer;
        }
        while (cap < size) {
            cap *= 2;
        }
        buffer.clear();
        return ByteBuffer.allocate(size);
    }

    private HdfsResponse doOpen(HdfsRequest request) throws IOException {
        String requestPath = request.getPath();
        Path path = new Path(requestPath);

        FileSystem fs = FileSystem.get(URI.create(requestPath), configuration);
        fs.setWorkingDirectory(new Path("/"));

        CacheValue cv = new CacheValue();
        cv.fs = fs;
        cv.path = path;
        cv.inputStream = fs.open(path);
        cv.buffer = newBuffer(1024 * 1024);

        String sessionId = UUID.randomUUID().toString();
        cache.put(sessionId, cv);
        HdfsResponse resp = HdfsResponse.newBuilder().setSessionId(sessionId).build();
        return resp;
    }

    private HdfsResponse doClose(HdfsRequest request) {
        cache.invalidate(request.getSessionId());
        System.out.printf("cache size = %d\n", cache.size());
        return HdfsResponse.getDefaultInstance();
    }

    private CacheValue getCacheValue(String sessionId) throws IOException {
        CacheValue cv = cache.getIfPresent(sessionId);
        if (cv == null) {
            throw new IOException(String.format("session id %s not found", sessionId));
        }
        return cv;
    }

    private HdfsResponse doRead(HdfsRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        cv.buffer = resizeBuffer(cv.buffer, request.getSize());
        cv.inputStream.read(0, cv.buffer.array(), request.getOffset(), request.getSize());
        ByteString bs = ByteString.copyFrom(cv.buffer, request.getSize());
        HdfsResponse resp = HdfsResponse.newBuilder().setData(bs).build();
        return resp;
    }

    private HdfsResponse doGetSize(HdfsRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        FileStatus st = cv.fs.getFileStatus(cv.path);
        HdfsResponse resp = HdfsResponse.newBuilder().setSize(st.getLen()).build();
        return resp;
    }

    private HdfsResponse doGetStats(HdfsRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        HdfsStats.Builder stats = HdfsStats.newBuilder();

        if (cv.inputStream instanceof HdfsDataInputStream) {
            HdfsDataInputStream inputStream = (HdfsDataInputStream) cv.inputStream;
            DFSInputStream.ReadStatistics st = inputStream.getReadStatistics();
            stats.setTotalBytesRead(st.getTotalBytesRead())
                    .setTotalLocalBytesRead(st.getTotalLocalBytesRead())
                    .setTotalShortCircuitBytesRead(st.getTotalShortCircuitBytesRead());
        }
        HdfsResponse resp = HdfsResponse.newBuilder().setStats(stats).build();
        return resp;
    }

    // ============================================================

    @Override
    public void hdfsOpen(HdfsRequest request, StreamObserver<HdfsResponse> responseObserver) {
        try {
            responseObserver.onNext(doOpen(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void hdfsClose(HdfsRequest request, StreamObserver<HdfsResponse> responseObserver) {
        responseObserver.onNext(doClose(request));
        responseObserver.onCompleted();
    }

    @Override
    public void hdfsRead(HdfsRequest request, StreamObserver<HdfsResponse> responseObserver) {
        try {
            responseObserver.onNext(doRead(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void hdfsGetSize(HdfsRequest request, StreamObserver<HdfsResponse> responseObserver) {
        try {
            responseObserver.onNext(doGetSize(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void hdfsGetStats(HdfsRequest request, StreamObserver<HdfsResponse> responseObserver) {
        try {
            responseObserver.onNext(doGetStats(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }
}
