package com.dirlt.java.jni;

public class CalledByNative {
    public static void greet() {
        System.out.println("greeted by CalledByNative");
    }

    public static void main(String[] args) {
        CalledByNative.greet();
    }
}
