package com.dirlt.java.scopedtimer;

public class ScopedTimer implements AutoCloseable {
    private String name;
    private long start;

    public ScopedTimer(String name) {
        this.name = name;
        start = System.currentTimeMillis();
    }

    public void close() {
        long t = System.currentTimeMillis() - start;
        System.out.printf("logging. name = %s, value = %dms\n", name, t);
    }
}
