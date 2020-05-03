package com.dirlt.java.playground;

import java.util.Iterator;
import java.util.TreeSet;

/**
 * Created with IntelliJ IDEA.
 * User: dirlt
 * Date: 3/25/13
 * Time: 11:42 AM
 * To change this template use File | Settings | File Templates.
 */
public class FixedSizeHeap<E> {
    private TreeSet<E> set;
    private int size;

    public FixedSizeHeap(int size) {
        this.size = size;
        set = new TreeSet<E>();
    }

    public void add(E e) {
        set.add(e);
        if (set.size() > size) {
            set.remove(set.last());
        }
    }

    public Iterator<E> iterator() {
        return set.iterator();
    }

    public static void main(String[] args) {
        FixedSizeHeap<Integer> heap = new FixedSizeHeap<Integer>(3);
        heap.add(10);
        heap.add(20);
        heap.add(5);
        heap.add(30);
        Iterator<Integer> iterator = heap.iterator();
        while(iterator.hasNext()) {
            Integer a = iterator.next();
            System.out.println(a);
        }
    }
}
