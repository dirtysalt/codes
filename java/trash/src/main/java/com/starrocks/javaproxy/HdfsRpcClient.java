package com.starrocks.javaproxy;

import com.dirlt.java.grpc.examples.helloworld.HelloWorldClient;
import io.grpc.Channel;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

public class HdfsRpcClient {

    private static final Logger logger = Logger.getLogger(HelloWorldClient.class.getName());

    private final PInternalServiceGrpc.PInternalServiceBlockingStub blockingStub;

    public HdfsRpcClient(Channel channel) {
        blockingStub = PInternalServiceGrpc.newBlockingStub(channel);
    }

    public void test(String path) {
        HdfsRequest request = HdfsRequest.newBuilder().setPath(path).build();
        HdfsResponse resp = blockingStub.hdfsOpen(request);
        String sessionId = resp.getSessionId();
        System.out.println("Session Id = " + sessionId);

        // get size, read, get stats
        {
            request = HdfsRequest.newBuilder().setSessionId(sessionId).setOffset(0).setSize(12).build();
            resp = blockingStub.hdfsGetSize(request);
            System.out.printf("size = %d\n", resp.getSize());

            resp = blockingStub.hdfsRead(request);
            String ss = resp.getData().toString();
            System.out.printf("data = %s\n", ss);

            resp = blockingStub.hdfsGetStats(request);
            System.out.printf("stats = %d\n", resp.getStats().getTotalBytesRead());
        }

        request = HdfsRequest.newBuilder().setSessionId(sessionId).build();
        blockingStub.hdfsClose(request);
    }

    public static void main(String[] args) throws Exception {
        String target = "localhost:50051";
        String path = "file:///Users/dirlt/.ssh/id_rsa.pub";
        if (args.length > 0) {
            path = args[0];
        }
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target)
                .usePlaintext().build();
        try {
            HdfsRpcClient client = new HdfsRpcClient(channel);
            client.test(path);
        } finally {
            // ManagedChannels use resources like threads and TCP connections. To prevent leaking these
            // resources the channel should be shut down when it will no longer be used. If it may be used
            // again leave it running.
            channel.shutdownNow().awaitTermination(5, TimeUnit.SECONDS);
        }
    }
}
