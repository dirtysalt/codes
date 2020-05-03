package com.dirlt.java.playground;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 8/8/13
 * Time: 11:10 AM
 * To change this template use File | Settings | File Templates.
 */
public class HyperLogLog {
    private int[] max_zeroes;

    public HyperLogLog(int bucket) {
        max_zeroes = new int[1 << bucket];
    }

    public HyperLogLog() {
        this(8);
    }

    public int[] getVector() {
        return max_zeroes;
    }

    public static int hash32(final byte[] data, int length, int seed) {
        // 'm' and 'r' are mixing constants generated offline.
        // They're not really 'magic', they just happen to work well.
        final int m = 0x5bd1e995;
        final int r = 24;
        // Initialize the hash to a random value
        int h = seed ^ length;
        int length4 = length / 4;

        for (int i = 0; i < length4; i++) {
            final int i4 = i * 4;
            int k = (data[i4 + 0] & 0xff) + ((data[i4 + 1] & 0xff) << 8)
                    + ((data[i4 + 2] & 0xff) << 16)
                    + ((data[i4 + 3] & 0xff) << 24);
            k *= m;
            k ^= k >>> r;
            k *= m;
            h *= m;
            h ^= k;
        }

        // Handle the last few bytes of the input array
        switch (length % 4) {
            case 3:
                h ^= (data[(length & ~3) + 2] & 0xff) << 16;
            case 2:
                h ^= (data[(length & ~3) + 1] & 0xff) << 8;
            case 1:
                h ^= (data[length & ~3] & 0xff);
                h *= m;
        }

        h ^= h >>> 13;
        h *= m;
        h ^= h >>> 15;

        return h;
    }

    public static long hash(byte[] bs) {
        int code = hash32(bs, bs.length, 0);
        return (code & 0x0ffffffffL);
    }

    public static int trailing_zero_count(int value) {
        if (value == 0) {
            return 32;
        }
        int p = 0;
        while (((value >> p) & 1) == 0) {
            p += 1;
        }
        return p;
    }

    public void sinkId(byte[] bs) {
        long h = hash(bs);
        int bucket = (int) (h % max_zeroes.length);
        int bucket_hash = (int) (h / max_zeroes.length);
        max_zeroes[bucket] = Math.max(max_zeroes[bucket], trailing_zero_count(bucket_hash));
    }

    public void sinkId(String s) {
        sinkId(s.getBytes());
    }

    public boolean sinkVector(int[] vector) {
        if (vector.length != max_zeroes.length) {
            return false;
        }
        for (int i = 0; i < vector.length; i++) {
            max_zeroes[i] = Math.max(max_zeroes[i], vector[i]);
        }
        return true;
    }

    public double getCardinality() {
        int sum = 0;
        for(int v:max_zeroes) {
            sum += v;
        }
        double exp = sum * 1.0 / max_zeroes.length;
        return Math.pow(2.0,exp) * max_zeroes.length * 0.79402;
    }

    public static void main(String[] args) throws Exception {
        // read lines from stdin.
        HyperLogLog hyperLogLog = new HyperLogLog();
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            String s = reader.readLine();
            if(s==null) {
                break;
            }
            hyperLogLog.sinkId(s);
        }
        int[] vector = hyperLogLog.getVector();
        for(int v:vector) {
            System.out.print(v + " ");
        }
        System.out.println("");
        System.out.printf("%.3f\n",hyperLogLog.getCardinality());
    }
}
