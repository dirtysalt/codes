/*
 * Copyright (C) dirlt
 */

#include <pthread.h>
#include "share/queue.h"
#include "share/lock.h"
#include "share/cond.h"
#include "share/util.h"

using namespace share;

class BPQItem {
public:
    BPQItem(int id = -1): id_(id) {}
    bool operator<(const BPQItem& a) const {
        return id_ < a.id_;
    }
    int id_;
}; // class BPQItem

class SLQItem {
public:
    SLQItem(int id = -1): id(id) {}
    int id;
    SLQItem* next;
}; // class SLQItem

class DLQItem {
public:
    DLQItem(int id = -1): id(id) {}
    int id;
    DLQItem* prev;
    DLQItem* next;
}; // class DLQItem

int main() {
    // BlockingQueue
    {
        BlockingQueue< int >bq;
        int v = 0;
        assert(bq.pop(&v, 100) == false);
        bq.push(1);
        assert(bq.pop(&v, 10));
        assert(v == 1);
    }
    // BlockingDLinkedListQueue
    {
        DLQItem* p = NULL;
        BlockingDLinkedListQueue< DLQItem* > bdlq;
        bdlq.push(new DLQItem(1));
        assert(bdlq.pop(&p, 0));
        assert(p->id == 1);
        delete p;
        bdlq.push(new DLQItem(1));
        bdlq.push_front(new DLQItem(2));
        assert(bdlq.pop(&p, 0));
        assert(p->id == 2);
        delete p;
        assert(bdlq.pop(&p, 0));
        assert(p->id == 1);
        delete p;
    }
    // BlockingPriorityQueue
    {
        BlockingPriorityQueue< BPQItem > pq;
        pq.push(BPQItem(10));
        pq.push(BPQItem(9));
        BPQItem a;
        assert(pq.pop(&a));
        BPQItem b;
        assert(pq.pop(&b));
        assert(a.id_ == 10);
        assert(b.id_ == 9);
        assert(!pq.pop(&a, 1));
    }
    // SLinkedListQueue
    {
        SLQItem* p = NULL;
        SLinkedListQueue< SLQItem* > slq;
        slq.push(new SLQItem(1));
        p = slq.pop();
        assert(p->id == 1);
        delete p;
        slq.push(new SLQItem(1));
        slq.push_front(new SLQItem(2));
        p = slq.pop();
        assert(p->id == 2);
        delete p;
        p = slq.pop();
        assert(p->id == 1);
        delete p;
    }
    // DLinkedListQueue
    {
        DLQItem* p = NULL;
        DLinkedListQueue< DLQItem* > dlq;
        dlq.push(new DLQItem(1));
        p = dlq.pop();
        assert(p->id == 1);
        delete p;
        dlq.push(new DLQItem(1));
        dlq.push_front(new DLQItem(2));
        p = dlq.pop();
        assert(p->id == 2);
        delete p;
        p = dlq.pop();
        assert(p->id == 1);
        delete p;


        dlq.push(new DLQItem(1));
        DLQItem* q = new DLQItem(2);
        dlq.push(q);
        dlq.push(new DLQItem(3));
        DLQItem* u = new DLQItem(4);
        dlq.replace(q, u);
        delete q;
        p = dlq.pop();
        assert(p->id == 1);
        delete p;
        p = dlq.pop();
        assert(p->id == 4);
        delete p;
        p = dlq.pop();
        assert(p->id == 3);
        delete p;
    }
    // SyncedQueue
    {
        SyncedQueue< SLinkedListQueue< SLQItem* >, SLQItem*, NopLock, NopCondition >q;
        q.push(new SLQItem(1));
        SLQItem* p = NULL;
        assert(q.pop(&p));
        assert(p->id == 1);
    }
    {
        SyncedQueue< STLQueue<int>, int , SpinLock, FutexCondition > q;
        q.push(1);
        assert(q.pop(NULL, 1));
        // 2 secs.
        printf("wait 2 secs...\n");
        assert(q.pop(NULL, 2000) == false);
    }
    return 0;
}
