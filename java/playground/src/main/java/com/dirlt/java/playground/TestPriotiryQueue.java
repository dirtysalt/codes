package com.dirlt.java.playground;

import java.util.Iterator;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 3/20/13
 * Time: 6:56 PM
 * To change this template use File | Settings | File Templates.
 */
public class TestPriotiryQueue {
    static class Item implements Comparable<Item> {
        Long value;

        public Item(Long value) {
            this.value = value;
        }

        @Override
        public int compareTo(Item item) {
            if (value < item.value) {
                return 1;
            } else if (value > item.value) {
                return -1;
            } else {
                return 0;
            }
        }
    }

    public static void main(String[] args) {
        FixedSizeHeap<Item> pq = new FixedSizeHeap<Item>(2);
        pq.add(new Item((long)10));
        pq.add(new Item((long)30));
        pq.add(new Item((long)20));
        pq.add(new Item((long)1461));
        pq.add(new Item((long)3835));
        pq.add(new Item((long)12345));
        Iterator<Item> iterator = pq.iterator();
        while(iterator.hasNext()) {
            Item item = iterator.next();
            System.out.println(item.value);
        }
    }
}
