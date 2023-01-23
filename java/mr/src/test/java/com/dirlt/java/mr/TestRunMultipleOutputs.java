package com.dirlt.java.mr;

import junit.framework.Assert;
import junit.framework.TestCase;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mrunit.mapreduce.MapDriver;

import java.io.IOException;
import java.util.List;
import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/13/12
 * Time: 1:49 PM
 * To change this template use File | Settings | File Templates.
 */

public class TestRunMultipleOutputs extends TestCase {
    MapDriver<LongWritable, Text, NullWritable, NullWritable> driver = null;
    RunMultipleOutputs._Mapper mapper = null;
    MockMultipleOutput<?, ?> mos = null;

    @Override
    public void setUp() {
        driver = new MapDriver<LongWritable, Text, NullWritable, NullWritable>();
        mapper = new RunMultipleOutputs._Mapper();
        driver.setMapper(mapper);
        mos = new MockMultipleOutput();
        mapper.setMultipleOutputs(mos);
    }

    public void testSample() throws IOException, InterruptedException {
        driver.withInput(new LongWritable(0), new Text("hello"));
        driver.run();
        Map<String, List<MultipleOutputsInterface._Pair<?, ?>>> output = mos.getOutput();
        List<MultipleOutputsInterface._Pair<?, ?>> outf = output.get("f");
        Assert.assertEquals(outf.size(), 1);
        MultipleOutputsInterface._Pair<?, ?> kv = outf.get(0);
        Text k = (Text) kv.getKey();
        Text v = (Text) kv.getValue();
        // nice.
        Assert.assertEquals(k.toString(), "fk");
        Assert.assertEquals(v.toString(), "hello");
    }
}
