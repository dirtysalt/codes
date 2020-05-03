package com.dirlt.java.voldemort;

import voldemort.client.ClientConfig;
import voldemort.client.SocketStoreClientFactory;
import voldemort.client.StoreClient;
import voldemort.client.StoreClientFactory;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 10/30/13
 * Time: 3:26 PM
 * To change this template use File | Settings | File Templates.
 */
public class SimpleQuery {
    // just on single node.
    public static void main(String[] args) {
        StoreClientFactory factory = new SocketStoreClientFactory(new ClientConfig().setBootstrapUrls("tcp://localhost:6666"));
        StoreClient client = factory.getStoreClient("test");
        client.put("k", "v");
        String v = (String) (client.get("k").getValue());
        System.out.println(v);
        factory.close();
    }
}
