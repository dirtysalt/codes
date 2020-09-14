package com.dirlt.java.mr;

import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 1:07 PM
 * To change this template use File | Settings | File Templates.
 */

// multiple outputs don't work well with MRUnit. so I have to mock one.
public interface MultipleOutputsInterface<KEYOUT, VALUEOUT> {
    public static class _Pair<K, V> {
        private K key;
        private V value;

        public _Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }

    public <K, V> void write(String name, K k, V v) throws IOException, InterruptedException;

    public <K, V> void write(String name, K k, V v, String basePath) throws IOException, InterruptedException;

    public <K, V> void close() throws IOException, InterruptedException;

    public Map<String, List<_Pair<?, ?>>> getOutput();
}
