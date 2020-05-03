package com.dirlt.java.guava;

import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;

import java.util.concurrent.TimeUnit;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/7/12
 * Time: 11:03 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestCacheBuilder {
    public static void testLoadingCache() throws Exception {
        CacheBuilder cb = CacheBuilder.newBuilder();
        LoadingCache<String, String> lc = cb.build(new CacheLoader<String, String>() {
            @Override
            public String load(String key) {
                // identity.
                return key;
            }
        });
        // if not exists. just return identity
        System.out.println(lc.get("hello"));
        lc.put("hello", "world");
        // just return value. world
        System.out.println(lc.get("hello"));
    }

    public static void testCache() throws Exception {
        CacheBuilder cb = CacheBuilder.newBuilder();
        cb.maximumSize(10);
        cb.expireAfterWrite(1, TimeUnit.SECONDS);
        Cache<String, String> cache = cb.build();
        cache.put("hello", "world");
        System.out.println(cache.getIfPresent("hello"));
        Thread.sleep(1000); // 1s.
        if (cache.getIfPresent("hello") == null) {
            System.out.println("already evicted");
        }
    }

    public static void main(String[] args) throws Exception {
        // really nice.
        testLoadingCache();
        testCache();
    }
}
