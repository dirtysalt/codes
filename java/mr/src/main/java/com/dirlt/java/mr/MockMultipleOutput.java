package com.dirlt.java.mr;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 1:19 PM
 * To change this template use File | Settings | File Templates.
 */
public class MockMultipleOutput<KEYOUT, VALUEOUT> implements MultipleOutputsInterface<KEYOUT, VALUEOUT> {
    private Map<String, List<_Pair<?, ?>>> store;

    public MockMultipleOutput() {
        store = new TreeMap<String, List<_Pair<?, ?>>>();
    }

    public <K, V> void write(String name, K key, V value) {
        List<_Pair<?, ?>> list = null;
        if (store.containsKey(name)) {
            list = store.get(name);
        } else {
            list = new LinkedList<_Pair<?, ?>>();
            store.put(name, list);
        }
        list.add(new _Pair<K, V>(key, value));
    }

    public <K, V> void write(String name, K key, V value, String basePath) {
        write(name + "/" + basePath, key, value);
    }

    public void close() {

    }

    public Map<String, List<_Pair<?, ?>>> getOutput() {
        return store;
    }
}
