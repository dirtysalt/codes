package com.dirlt.java.memcached;

import net.spy.memcached.AddrUtil;
import net.spy.memcached.MemcachedClient;
import net.spy.memcached.internal.GetFuture;
import net.spy.memcached.internal.OperationFuture;

import java.io.IOException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class AsyncMemcached {
    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException, TimeoutException {
        MemcachedClient client = new MemcachedClient(AddrUtil.getAddresses("localhost:11211"));
        System.out.println("connected...");
        OperationFuture<Boolean> putFuture = client.set("hello", 60, "world");     // use future pool to accomplish async task.
        GetFuture<Object> getFuture = client.asyncGet("hello");
        String value = (String) getFuture.get(3, TimeUnit.SECONDS);
        assert value.equals("world");
    }
}
