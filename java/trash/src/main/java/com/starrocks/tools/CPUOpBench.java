package com.starrocks.tools;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import java.util.Random;

public class CPUOpBench {
    private final static Logger logger = LogManager.getLogger(CPUOpBench.class.getCanonicalName());

    public static void test(int arraySize, int N) {
        // in L1 Cache.
        int data[] = new int[arraySize];
        Random rnd = new Random(42);
        for (int i = 0; i < arraySize; i++) {
            data[i] = rnd.nextInt();
        }
        long start = System.currentTimeMillis();

        long chksum = 0x7f7f7f7f;
        for (int i = 0; i < N; i++) {
            long sum = 0;
            for (int j = 0; j < arraySize; j++) {
                sum += data[j];
            }
            chksum = chksum ^ sum;
            chksum = chksum ^ (long) i;
        }

        long end = System.currentTimeMillis();
        long duration = end - start;
        logger.info(String.format("checksum = %d, duration = %dms, avg = %.2fus", chksum, duration,
                duration * 1000.f / (N)));
    }

    public static void main(String[] args) {
        // fit in L1 Cache
        int arraySize = 8 * 1024;
        int N = 1;
        int round = 20;

        String value = null;
        for (int i = 0; i < args.length; ) {
            String opt = args[i];
            if ((i + 1) < args.length) {
                value = args[i + 1];
            }
            if (opt.equals("-R")) {
                round = Integer.parseInt(value);
            } else if (opt.equals("-N")) {
                N = Integer.parseInt(value);
            } else {
                i -= 1;
            }
            i += 2;
        }
        System.out.printf("%s -R %d -N %d\n", CPUOpBench.class.getName(), round, N);
        N *= 1000000;
        for (int i = 0; i < round; i++) {
            test(arraySize, N);
        }
    }
}
