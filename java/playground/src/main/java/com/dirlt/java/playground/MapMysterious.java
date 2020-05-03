package com.dirlt.java.playground;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 1/10/13
 * Time: 6:16 PM
 * To change this template use File | Settings | File Templates.
 */
public class MapMysterious {
    public static void foo() {
        Integer x = new Integer(10);
        x += 20;
        System.out.println(x.intValue());

        Map<String, Integer> dict = new HashMap<String, Integer>();
        dict.put("hello", 0);
        Integer y = dict.get("hello");
        y += 30;
        System.out.println(dict.get("hello"));
    }

    public static void bar() {
        Map<String, List<String>> dict = new HashMap<String, List<String>>();
        List<String> s = new LinkedList<String>();
        s.add("world");
        dict.put("hello", s);

        s.add("world2");
        for (String x : dict.get("hello")) {
            System.out.println(x);
        }
    }

    public static void main(String[] args) {
        foo();
        bar();
    }
}
