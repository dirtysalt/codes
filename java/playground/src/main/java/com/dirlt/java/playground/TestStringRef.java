package com.dirlt.java.playground;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/6/12
 * Time: 10:37 AM
 * To change this template use File | Settings | File Templates.
 */
public class TestStringRef {
    public static void foo(String a) {
        a="hello";
    }

    public static void main(String[] args) {
        String a = "world";
        foo(a);
        System.out.println(a);
    }
}
