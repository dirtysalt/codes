package com.starrocks.tools;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class S3Bench {
    public static class LatencyStats {
        public List<Long> values;
        private int threads = 0;

        public LatencyStats() {
            values = new ArrayList<>();
        }

        public void print(boolean summary) {
            Collections.sort(values);
            int size = values.size();
            long sum = values.stream().reduce(0L, Long::sum);
            int t = threads == 0 ? 1 : threads;
            float iops = t * size * 1000.f / sum;
            float avg = sum * 1.0f / size;
            long p00 = values.get(0);
            long p50 = values.get(size / 2);
            long p90 = values.get(size * 90 / 100);
            long p99 = values.get(size * 99 / 100);
            long p100 = values.get(size - 1);
            String sep = " - ";
            if (summary) {
                sep = "\n";
            }
            System.out.printf(
                    "IOPS: %.2f(T=%d, %d / %dms)%sLatency: avg = %.2fms, min = %dms, p50 = %dms, p90 = %dms, p99 = %dms, max = %dms\n",
                    iops, t, size, sum, sep, avg, p00, p50, p90, p99, p100);
            if (summary) {
                String[] attrs = {"IOPS", "AVG", "MIN", "P50", "P90", "P99", "MAX"};
                System.out.println(String.join(",", attrs));
                System.out.printf("%.2f,%.2fms,%dms,%dms,%dms,%dms,%dms\n", iops, avg, p00, p50, p90, p99, p100);
            }
        }

        public void merge(LatencyStats stats) {
            threads += 1;
            values.addAll(stats.values);
        }
    }

    public static class Runner implements Runnable {
        public LatencyStats stats;

        ObjectClient client;
        String bucket;
        List<ObjectClient.ObjectMeta> metaList;
        int round;
        int repeat;
        int block_size;
        int scan_size;

        public Runner(ObjectClient client, String bucket, List<ObjectClient.ObjectMeta> metaList, int round,
                      int repeat, int block_size, int scan_size) {
            this.client = client;
            this.bucket = bucket;
            this.metaList = metaList;
            this.round = round;
            this.repeat = repeat;
            this.block_size = block_size;
            this.scan_size = scan_size;
            this.stats = new LatencyStats();
        }

        @Override
        public void run() {
            Random rnd = new Random();
            while (round > 0) {
                round--;
                int idx = rnd.nextInt(Integer.SIZE - 1) % metaList.size();
                {
                    ObjectClient.ObjectMeta meta = metaList.get(idx);
                    String keyName = meta.name;
                    long fileSize = Math.min(meta.size, scan_size);
                    for (int i = 0; i < repeat; i++) {
                        // make sure there are enough bytes.
                        long offset = rnd.nextInt(Integer.SIZE - 1) % (fileSize - block_size - 1);
                        long ss = System.currentTimeMillis();
                        try {
                            byte[] data = client.readObject(bucket, keyName, offset, block_size);
                            if (data == null) {
                                return;
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                            return;
                        }
                        long ee = System.currentTimeMillis();
                        long t = ee - ss;
                        stats.values.add(t);
                    }
                }
            }
            stats.print(false);
        }
    }

    public static ObjectClient buildClient(String mode, String endpoint, String cred)
            throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        if (mode.equals("s3")) {
            return MyS3Client.build(endpoint, cred);
        } else if (mode.equals("oss")) {
            return MyOSSClient.build(endpoint, cred);
        } else if (mode.equals("hdfs")) {
            //            Class cls = Class.forName("com.starrocks.tools.MyHDFSClient");
            //            Method m = cls.getMethod("build", String.class);
            //            ObjectClient client = (ObjectClient) m.invoke(null, endpoint);
            //            return client;
            return MyHDFSClient.build(endpoint);
        } else {
            System.out.printf("unknown mode: %s%n", mode);
            return null;
        }
    }

    public static void main(String[] args)
            throws InterruptedException, IOException, ClassNotFoundException, InvocationTargetException,
            NoSuchMethodException, IllegalAccessException {
        int num_threads = 16;
        int repeat = 1;
        int block_size = 4;
        int round = 100;
        String value = null;
        String bucket = null;
        String path = null;
        String endpoint = "http://s3.ap-southeast-1.amazonaws.com";
        // "http://oss-cn-zhangjiakou-internal.aliyuncs.com";
        String cred = null;
        int scan_size = 200;
        String mode = "s3";
        for (int i = 0; i < args.length; ) {
            String opt = args[i];
            if ((i + 1) < args.length) {
                value = args[i + 1];
            }
            if (opt.equals("--repeat")) {
                repeat = Integer.parseInt(value);
            } else if (opt.equals("--block")) {
                block_size = Integer.parseInt(value);
            } else if (opt.equals("--thread")) {
                num_threads = Integer.parseInt(value);
            } else if (opt.equals("--round")) {
                round = Integer.parseInt(value);
            } else if (opt.equals("--bucket")) {
                bucket = value;
            } else if (opt.equals("--path")) {
                path = value;
            } else if (opt.equals("--cred")) {
                cred = value;
            } else if (opt.equals("--endpoint")) {
                endpoint = value;
            } else if (opt.equals("--scan")) {
                scan_size = Integer.parseInt(value);
            } else if (opt.equals("--mode")) {
                mode = value;
            } else {
                i -= 1;
            }
            i += 2;
        }

        System.out.printf(
                "%s --mode %s --endpoint %s --bucket %s --path %s --cred %s --thread %d --round %d --block %dKB --scan %dMB --repeat %d\n%n",
                S3Bench.class.getName(), mode, endpoint, bucket, path, cred, num_threads, round, block_size,
                scan_size, repeat);
        if (path == null) {
            System.out.println("path is null");
            return;
        }

        block_size *= 1024;
        scan_size *= (1024 * 1024);
        List<ObjectClient.ObjectMeta> metaList = new ArrayList<>();

        // Gather metadata of files.
        {
            ObjectClient client = S3Bench.buildClient(mode, endpoint, cred);
            if (client == null) {
                return;
            }

            if (!path.startsWith("@")) {
                // List objects in that bucket/path
                if (path.startsWith("/")) {
                    path = path.substring(1);
                }
                client.listObjects(bucket, path, metaList);
            } else {
                // file contains file names.
                BufferedReader buffer = new BufferedReader(new FileReader(path.substring(1)));
                while (true) {
                    String name = buffer.readLine();
                    if (name == null) {
                        break;
                    }
                    if (name.startsWith("/")) {
                        name = name.substring(1);
                    }
                    if (name.isEmpty()) {
                        continue;
                    }
                    client.headObject(bucket, name, metaList);
                }
            }
        }

        // Print files to scan.
        if (metaList.size() == 0) {
            System.out.println("No files to scan");
            return;
        }
        System.out.printf("==========  files  ==========\n");
        for (ObjectClient.ObjectMeta meta : metaList) {
            System.out.printf("scan %s -> %d bytes%n", meta.name, meta.size);
        }

        System.out.printf("==========  testing  ==========\n");
        // Generate threads to scan files
        List<Thread> threads = new ArrayList<>();
        List<Runner> runners = new ArrayList<>();
        LatencyStats stats = new LatencyStats();
        for (int i = 0; i < num_threads; i++) {
            ObjectClient client = buildClient(mode, endpoint, cred);
            Runner r =
                    new Runner(client, bucket, metaList, round, repeat, block_size, scan_size);
            runners.add(r);
            Thread t = new Thread(r);
            threads.add(t);
            t.start();
        }
        for (int i = 0; i < num_threads; i++) {
            threads.get(i).join();
            stats.merge(runners.get(i).stats);
        }
        System.out.printf("==========  summary  ==========\n");
        stats.print(true);
    }
}
