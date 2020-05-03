package com.dirlt.java.playground;

import javax.management.MBeanServer;
import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 4/26/13
 * Time: 11:25 AM
 * To change this template use File | Settings | File Templates.
 */
public class SimpleJMX implements SimpleJMXMBean {
    private int value = 0;

    public int getValue() {
        System.out.println("get value");
        return value;
    }

    public void setValue(int v) {
        System.out.println("set value");
        value = v;
    }

    public static void main(String[] args) throws Exception {
        MBeanServer mbs = ManagementFactory.getPlatformMBeanServer();
        ObjectName name = new ObjectName("com.dirlt.java.playground:type=SimpleJMX");
        SimpleJMXMBean mbean = new SimpleJMX();
        mbs.registerMBean(mbean, name);
        System.out.println("Waiting forever...");
        Thread.sleep(Long.MAX_VALUE);
    }
}
