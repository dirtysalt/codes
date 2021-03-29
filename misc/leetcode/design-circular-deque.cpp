/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <functional>
#include <thread>
#include <condition_variable>
#include <mutex>
using namespace std;

class MyCircularDeque {
    int * data;
    int front;
    int tail;
    int cap;
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        front = tail = 0;
        cap = k + 1;
        data =new int[cap];
    }
    ~MyCircularDeque() {
        delete [] data;
    }

    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if (isFull()) return false;
        data[front] = value;
        front = (front - 1 + cap) % cap;
        return true;
    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if (isFull()) return false;
        tail = (tail + 1 + cap) % cap;
        data[tail] = value;
        return true;
    }

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % cap;
        return true;
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if (isEmpty()) return false;
        tail = (tail - 1 + cap) % cap;
        return true;
    }

    /** Get the front item from the deque. */
    int getFront() {
        if (isEmpty()) return -1;
        return data[(front + 1) % cap];
    }

    /** Get the last item from the deque. */
    int getRear() {
        if (isEmpty()) return -1;
        return data[tail];
    }

    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return front == tail;

    }

    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return (tail + 1) % cap == front;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
