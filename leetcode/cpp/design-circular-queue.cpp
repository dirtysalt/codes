/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <iostream>
#include <map>
#include <memory>
#include <set>
#include <string>
#include <vector>
using namespace std;

#ifdef DEBUG
#define P(format, ...) printf(format, ##__VA_ARGS__)
#else
#define P(format, ...)
#endif

class MyCircularQueue {
  int *data;
  int front;
  int tail;
  int cap;

public:
  MyCircularQueue(int k) {
    data = new int[k + 1];
    front = 0;
    tail = -1;
    cap = k + 1;
  }
  ~MyCircularQueue() { delete[] data; }
  bool enQueue(int value) {
    if (isFull())
      return false;
    tail = (tail + 1) % cap;
    data[tail] = value;
    return true;
  }

  bool deQueue() {
    if (isEmpty())
      return false;
    front = (front + 1) % cap;
    return true;
  }

  int Front() {
    if (isEmpty())
      return -1;
    return data[front];
  }

  int Rear() {
    if (isEmpty())
      return -1;
    return data[tail];
  }

  bool isEmpty() { return (tail + 1) % cap == front; }

  bool isFull() { return (tail + 2) % cap == front; }

  void dump() {
    P("front = %d, tail = %d, data = [", front, tail);
    for (int i = 0; i < cap; i++) {
      P("%d ", data[i]);
    }
    P("]\n");
  }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */

int main() {
  auto q = MyCircularQueue(3);
  q.enQueue(1);
  q.enQueue(2);
  q.enQueue(3);
  q.enQueue(4);
  q.dump();
  P("rear = %d\n", q.Rear());
  return 0;
}