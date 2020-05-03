package com.dirlt.java.mysql;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class SQLInjector {
    // runnable.
    class Injector implements Runnable {
        private Connection connection;
        private String url;
        private String username;
        private String password;
        private boolean dryRun;

        private SQLInjector injector;

        public Injector(SQLInjector injector, String url, String username, String password, boolean dryRun) {
            this.url = url;
            this.username = username;
            this.password = password;
            this.injector = injector;
            this.dryRun = dryRun;
        }

        public Injector(SQLInjector injector, boolean dryRun) {
            this(injector, kURL, kUserName, kPassword, dryRun);
        }

        public void repeatableExec(String sql) throws SQLException {
            if (connection == null) {
                connection = DriverManager.getConnection(url, username, password);
            }
            PreparedStatement ps = connection.prepareStatement(sql);
            ps.execute();
            ps.close();
        }

        public void exec(String sql) {
            if (dryRun) {
                System.out.println(sql);
                return;
            }
            try {
                repeatableExec(sql);
            } catch (SQLException e) {
                if (e.getMessage().startsWith("Duplicate")) {
                    return;
                }
                // connection closed.
                if (connection != null) {
                    try {
                        connection.close();
                    } catch (SQLException e1) {

                    }
                }
                connection = null;
                try {
                    repeatableExec(sql);
                } catch (SQLException e2) {
                    e2.printStackTrace();
                }

            }
        }

        @Override
        public void run() {
            try {
                while (true) {
                    String sql = queue.poll(injector.pollTimeout, TimeUnit.MILLISECONDS);
                    if (sql == null) {
                        if (injector.exit) {
                            injector.refCount.decrementAndGet();
                            break;
                        }
                        continue;
                    }
                    exec(sql);
                }
            } catch (java.lang.InterruptedException e) {

            }
        }
    }

    public void start(String url, String username, String password, boolean dryRun) {
        exit = false;
        for (int i = 0; i < threadNumber; i++) {
            Injector injector = new Injector(this, url, username, password, dryRun);
            tp.submit(injector);
        }
    }

    public void feed(String filename) throws IOException, InterruptedException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filename)));
        String sql = null;
        int count = 0;
        while ((sql = reader.readLine()) != null) {
            queue.put(sql);
            count++;
            if ((count % 10000) == 0) {
                System.out.println("inject " + count + " records");
            }
        }
        exit = true;
        while (true) {
            if (refCount.get() == 0) {
                return;
            } else {
                Thread.sleep(pollTimeout);
            }
        }
    }

    public static final String kURL = "jdbc:mysql://localhost/umid2g";
    public static final String kUserName = "root";
    public static final String kPassword = "16021inthecloud";

    private static int kPollTimeout = 2000;
    private static int kBlockQueueSize = 2048;
    private static int kThreadNumber = 1;

    private int threadNumber;
    private int blockQueueSize;
    private int pollTimeout;

    // queue.
    private LinkedBlockingQueue<String> queue;
    // exit
    private volatile boolean exit = false;
    // ref count.
    private AtomicInteger refCount;
    // thread pool.
    private ExecutorService tp;

    public SQLInjector(int threadNumber, int blockQueueSize, int pollTimeout) {
        this.threadNumber = threadNumber;
        this.blockQueueSize = blockQueueSize;
        this.pollTimeout = pollTimeout;

        queue = new LinkedBlockingQueue<String>(blockQueueSize);
        refCount = new AtomicInteger(threadNumber);
        tp = new ThreadPoolExecutor(threadNumber, threadNumber, 0, TimeUnit.SECONDS, new LinkedBlockingQueue<Runnable>(blockQueueSize));
    }

    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        String filename = null;
        int threadNumber = kThreadNumber;
        int blockQueueSize = kBlockQueueSize;
        int pollTimeout = kPollTimeout;
        boolean dryRun = false;
        String url = kURL;
        String username = kUserName;
        String password = kPassword;
        for (String arg : args) {
            if (arg.startsWith("--filename=")) {
                filename = arg.substring("--filename=".length());
            } else if (arg.startsWith("--thread-number=")) {
                threadNumber = Integer.parseInt(arg.substring("--thread-number=".length()));
            } else if (arg.startsWith("--block-queue-size=")) {
                blockQueueSize = Integer.parseInt(arg.substring("--block-queue-size=".length()));
            } else if (arg.startsWith("--poll-timeout=")) {
                pollTimeout = Integer.parseInt(arg.substring("--poll-timeout=".length()));
            } else if (arg.startsWith("--dry-run")) {
                dryRun = true;
            } else if (arg.startsWith("--url=")) {
                url = arg.substring("--url=".length());
            } else if (arg.startsWith("--username=")) {
                username = arg.substring("--username=".length());
            } else if (arg.startsWith("--password=")) {
                password = arg.substring("--password=".length());
            }
        }
        SQLInjector injector = new SQLInjector(threadNumber, blockQueueSize, pollTimeout);
        injector.start(url, username, password, dryRun);
        injector.feed(filename);
        System.exit(0);
    }
}
