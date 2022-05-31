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

public class HDFSRpcHandler extends HDFSServiceGrpc.HDFSServiceImplBase {
    private static class CacheValue {
        public FileSystem fs;
        public Path path;
        public FSDataInputStream inputStream;
        public ByteBuffer buffer;
    }

    private Configuration configuration;
    private Cache<String, CacheValue> cache;

    public HDFSRpcHandler() {
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

    private HDFSResponse doOpen(HDFSRequest request) throws IOException {
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
        HDFSResponse resp = HDFSResponse.newBuilder().setSessionId(sessionId).build();
        return resp;
    }

    private HDFSResponse doClose(HDFSRequest request) {
        cache.invalidate(request.getSessionId());
        System.out.printf("cache size = %d\n", cache.size());
        return HDFSResponse.getDefaultInstance();
    }

    private CacheValue getCacheValue(String sessionId) throws IOException {
        CacheValue cv = cache.getIfPresent(sessionId);
        if (cv == null) {
            throw new IOException(String.format("session id %s not found", sessionId));
        }
        return cv;
    }

    private HDFSResponse doRead(HDFSRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        cv.buffer = resizeBuffer(cv.buffer, request.getSize());
        cv.inputStream.read(0, cv.buffer.array(), request.getOffset(), request.getSize());
        ByteString bs = ByteString.copyFrom(cv.buffer, request.getSize());
        HDFSResponse resp = HDFSResponse.newBuilder().setData(bs).build();
        return resp;
    }

    private HDFSResponse doGetSize(HDFSRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        FileStatus st = cv.fs.getFileStatus(cv.path);
        HDFSResponse resp = HDFSResponse.newBuilder().setSize(st.getLen()).build();
        return resp;
    }

    private HDFSResponse doGetStats(HDFSRequest request) throws IOException {
        CacheValue cv = getCacheValue(request.getSessionId());
        HDFSStats.Builder stats = HDFSStats.newBuilder();

        if (cv.inputStream instanceof HdfsDataInputStream) {
            HdfsDataInputStream inputStream = (HdfsDataInputStream) cv.inputStream;
            DFSInputStream.ReadStatistics st = inputStream.getReadStatistics();
            stats.setTotalBytesRead(st.getTotalBytesRead())
                    .setTotalLocalBytesRead(st.getTotalLocalBytesRead())
                    .setTotalShortCircuitBytesRead(st.getTotalShortCircuitBytesRead());
        }
        HDFSResponse resp = HDFSResponse.newBuilder().setStats(stats).build();
        return resp;
    }

    // ============================================================

    @Override
    public void open(HDFSRequest request, StreamObserver<HDFSResponse> responseObserver) {
        try {
            responseObserver.onNext(doOpen(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void close(HDFSRequest request, StreamObserver<HDFSResponse> responseObserver) {
        responseObserver.onNext(doClose(request));
        responseObserver.onCompleted();
    }

    @Override
    public void read(HDFSRequest request, StreamObserver<HDFSResponse> responseObserver) {
        try {
            responseObserver.onNext(doRead(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void getSize(HDFSRequest request, StreamObserver<HDFSResponse> responseObserver) {
        try {
            responseObserver.onNext(doGetSize(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }

    @Override
    public void getStats(HDFSRequest request, StreamObserver<HDFSResponse> responseObserver) {
        try {
            responseObserver.onNext(doGetStats(request));
        } catch (IOException e) {
            responseObserver.onError(e);
        }
        responseObserver.onCompleted();
    }
}
