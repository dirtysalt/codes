package com.dirlt.java.asynchbase;

import com.stumbleupon.async.Callback;
import com.stumbleupon.async.Deferred;
import org.hbase.async.GetRequest;
import org.hbase.async.HBaseClient;
import org.hbase.async.KeyValue;
import org.hbase.async.PutRequest;

import java.util.ArrayList;

public class AsyncHBase {
    public static class Bytes {
        public static byte[] toBytes(String s) {
            return s.getBytes();
        }

        public static String toString(byte[] bs) {
            return new String(bs);
        }
    }

    private static final String quorum = "localhost:2181";
    private static HBaseClient client = new HBaseClient(quorum);
    private static final String table = "t1";
    private static final String cf = "cf";

    public static void main(String[] args) throws Exception {
        // request1
        {
            System.out.println("start request1");
            PutRequest put = new PutRequest(Bytes.toBytes(table),
                    Bytes.toBytes("r1"), Bytes.toBytes(cf), Bytes.toBytes("key"),
                    Bytes.toBytes("value"));
            Deferred<Object> putFuture = client.put(put);
            putFuture.addCallback(new Callback<Object, Object>() {
                public Object call(Object obj) {
                    // put over. try to get it.
                    GetRequest get = new GetRequest(Bytes.toBytes(table), Bytes.toBytes("r1"));
                    get.family(cf).qualifier("key");
                    Deferred<ArrayList<KeyValue>> getFuture = client.get(get);
                    try {
                        Thread.sleep(5000);
                    } catch (Exception e) {

                    }
                    getFuture.addCallback(new Callback<Object, ArrayList<KeyValue>>() {
                        // get over. try to validate it.
                        public Object call(ArrayList<KeyValue> kvs) {
                            assert (kvs.size() == 1);
                            KeyValue kv = kvs.get(0);
                            assert (Bytes.toString(kv.value()).equals("value"));
                            System.out.println("finish request1");


//                            // before call shutdown, we raise another request.
//                            {
//                                System.out.println("start request2");
//                                PutRequest put = new PutRequest(Bytes.toBytes(table),
//                                        Bytes.toBytes("r2"), Bytes.toBytes(cf), Bytes.toBytes("key"),
//                                        Bytes.toBytes("value"));
//                                Deferred<Object> putFuture = client.put(put);
//                                putFuture.addCallback(new Callback<Object, Object>() {
//                                    public Object call(Object obj) {
//                                        // put over. try to get it.
//                                        GetRequest get = new GetRequest(Bytes.toBytes(table), Bytes.toBytes("r2"));
//                                        get.family(cf);
//                                        //qualifier("key");
//                                        Deferred<ArrayList<KeyValue>> getFuture = client.get(get);
//                                        getFuture.addCallback(new Callback<Object, ArrayList<KeyValue>>() {
//                                            // get over. try to validate it.
//                                            public Object call(ArrayList<KeyValue> kvs) {
//                                                assert (kvs.size() == 1);
//                                                KeyValue kv = kvs.get(0);
//                                                assert (Bytes.toString(kv.value()).equals("value"));
//                                                System.out.println("finish request2");
//                                                System.out.println("called shutdown after request2");
//                                                client.shutdown();
//                                                return null;
//                                            }
//                                        });
//                                        return null;
//                                    }
//                                });
//                            }
                            // doesn't matter because we already init a request.
                            System.out.println("called shutdown after request1");
                            client.shutdown();
                            return null;
                        }
                    });
                    return null;
                }
            });
        }
    }
}
