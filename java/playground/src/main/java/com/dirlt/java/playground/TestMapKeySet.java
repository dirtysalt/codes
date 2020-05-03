package com.dirlt.java.playground;

import java.util.*;

public class TestMapKeySet {
    public static void main(String[] args) {
        Map<String, String> dict = new HashMap<String, String>();

        System.out.println("----session1-----");
        dict.put("hello", "world");
        Set<String> ks = dict.keySet();
        for (String k : ks) {
            System.out.println(k);
        }

        System.out.println("----session2-----");
        dict.put("hello2", "world2");
        ks = dict.keySet();
        for (String k : ks) {
            System.out.println(k);
        }
    }
}
