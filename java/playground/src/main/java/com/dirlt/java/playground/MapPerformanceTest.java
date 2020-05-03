package com.dirlt.java.playground;

import java.util.HashMap;
import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 3/12/13
 * Time: 5:26 PM
 * To change this template use File | Settings | File Templates.
 */
public class MapPerformanceTest {
    private static final int NUMBER = 10000000;
    private static final String PREFIX = "s";
    private static final int kWarmupCount = 10;

    public static void action() {
        long start = System.currentTimeMillis();
        Map<String, Long> dict = new HashMap<String, Long>();
        for (int i = 0; i < NUMBER; i++) {
            dict.put(PREFIX + i, (long) i);
        }
        for (int i = 0; i < NUMBER; i++) {
            dict.put(PREFIX + i, dict.get(PREFIX + i) + dict.get(PREFIX + (i + 1000) % NUMBER));
        }
        long end = System.currentTimeMillis();
        System.out.printf("%.2f\n", (float) (end - start));
    }

    public static void action2() {
        long start = System.currentTimeMillis();
        Map<Integer, Long> dict = new HashMap<Integer, Long>();
        for (int i = 0; i < NUMBER; i++) {
            dict.put(i, (long) i);
        }
        for (int i = 0; i < NUMBER; i++) {
            dict.put(i, dict.get(i) + dict.get((i + 1000) % NUMBER));
        }
        long end = System.currentTimeMillis();
        System.out.printf("%.2f\n", (float) (end - start));
    }

    public static void main(String[] args) {
        for (int i = 0; i < kWarmupCount; i++) {
            System.out.printf("warm action #%d\n", i);
            action();
        }
        System.gc();
        System.out.printf("run action\n");
        action();

        for (int i = 0; i < kWarmupCount; i++) {
            System.out.printf("warm action2 #%d\n", i);
            action2();
        }
        System.gc();
        System.out.printf("run action2\n");
        action2();
    }
}

