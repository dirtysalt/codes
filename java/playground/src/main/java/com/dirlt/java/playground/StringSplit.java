package com.dirlt.java.playground;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/11/12
 * Time: 12:19 PM
 * To change this template use File | Settings | File Templates.
 */
public class StringSplit {
    public static void main(String[] args) {
        String s = "hello_";
        String[] ss = s.split("_");
        System.out.println(ss[0]);
    }
}
