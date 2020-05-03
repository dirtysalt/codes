package com.dirlt.java.playground;

import com.clearspring.analytics.stream.cardinality.HyperLogLogPlus;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 8/20/13
 * Time: 8:00 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestHyperLogLogPlus {
    public static void main(String[] args) throws Exception {
        // read lines from stdin.
        HyperLogLogPlus hyperLogLogPlus = new HyperLogLogPlus(14, 20);
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s = reader.readLine();
            if (s == null) {
                break;
            }
            hyperLogLogPlus.offer(s.getBytes());
        }
        byte[] bs = hyperLogLogPlus.getBytes();
        System.out.println("vector size = " + bs.length);
        System.out.println("estimate size = " + hyperLogLogPlus.cardinality());
    }
}
