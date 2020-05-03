package com.dirlt.java.playground;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 12/10/12
 * Time: 12:04 PM
 * To change this template use File | Settings | File Templates.
 */
public class ExceptionReturnValue {
    public static void main(String[] args) throws Exception {
        try {
            int i=0;
        }finally {
            System.out.println("got");
        }
        throw new Exception("Hello,World");
    }
}
