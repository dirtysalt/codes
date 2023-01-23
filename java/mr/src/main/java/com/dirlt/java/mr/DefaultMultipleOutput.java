package com.dirlt.java.mr;

import org.apache.hadoop.mapreduce.TaskInputOutputContext;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;

import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 1:09 PM
 * To change this template use File | Settings | File Templates.
 */
public class DefaultMultipleOutput<KEYOUT, VALUEOUT> implements MultipleOutputsInterface<KEYOUT, VALUEOUT> {
    private MultipleOutputs mos = null;

    public DefaultMultipleOutput(TaskInputOutputContext<?, ?, KEYOUT, VALUEOUT> context) {
        mos = new MultipleOutputs(context);
    }

    public <K, V> void write(String name, K key, V value) throws IOException, InterruptedException {
        mos.write(name, key, value);
    }

    public <K, V> void write(String name, K key, V value, String basePath) throws IOException, InterruptedException {
        mos.write(name, key, value, basePath);
    }

    public void close() throws IOException, InterruptedException {
        mos.close();
    }

    public Map<String, List<_Pair<?, ?>>> getOutput() {
        return null;
    }
}
