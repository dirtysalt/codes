package com.dirlt.java.jredis;

import org.jredis.connector.ConnectionSpec;
import org.jredis.ri.alphazero.JRedisAsyncClient;
import org.jredis.ri.alphazero.JRedisClient;
import org.jredis.ri.alphazero.JRedisFutureSupport;
import org.jredis.ri.alphazero.connection.DefaultConnectionSpec;

import java.util.concurrent.Future;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/7/12
 * Time: 11:59 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestAsyncOperation {
    private static final int kDefaultPort = 6379;
    private static final int kDefaultDB = 0;

    public static void testSync(ConnectionSpec spec) throws Exception {
        JRedisClient client = new JRedisClient(spec);
        client.set("hello", "world");
        String s = new String(client.get("hello"));
        System.out.println(s);
    }

    public static void testAsync(ConnectionSpec spec) throws Exception {
        // not implemented!!! WTF!!!
        JRedisAsyncClient client = new JRedisAsyncClient(spec);
        JRedisFutureSupport.FutureStatus fs = client.set("hello", "async");
        if (!fs.get().isError()) {
            System.out.println("async response message = " + fs.get().message());
            Thread.sleep(4000); // 4 seconds.
            System.out.println("start to fetch...,here we break server");
            Future<byte[]> f = client.get("hello");
            byte[] res = f.get();
            System.out.println(new String(res));
        }
    }

    public static void main(String[] args) throws Exception {
        ConnectionSpec spec = DefaultConnectionSpec.newSpec("localhost", kDefaultPort, kDefaultDB, null);
        testSync(spec);
        testAsync(spec);
    }
}
