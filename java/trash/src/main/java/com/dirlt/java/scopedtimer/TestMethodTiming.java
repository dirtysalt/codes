package com.dirlt.java.scopedtimer;

import com.google.inject.Guice;
import com.google.inject.Injector;

public class TestMethodTiming {
    public TestMethodTiming() {
    }

    @TimingScope("test")
    public void test() {
        System.out.println("test");
    }

    public void test2() {
        System.out.println("test2...");
    }

    public static void main(String[] args) {
        try (ScopedTimer st = new ScopedTimer("HiveMetaCache.partitions")) {
            Injector injector = Guice.createInjector(new TimingModule());
            TestMethodTiming t = injector.getInstance(TestMethodTiming.class);
            t.test();
            t.test2();
        }
    }

}
