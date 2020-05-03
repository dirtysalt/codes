package com.dirlt.java.playground;

import java.net.InetSocketAddress;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 8/13/13
 * Time: 7:30 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestInetSocketAddress {
    public static void main(String[] args) {
        InetSocketAddress address= new InetSocketAddress("hadoop1",12345);
        System.out.println(address.toString());
    }
}
