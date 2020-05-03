package com.dirlt.java.playground;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 8/15/13
 * Time: 11:15 AM
 * To change this template use File | Settings | File Templates.
 */
public class TestException {
    public static void main(String[] args) {
        try {
            throw new Exception("hello");
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
