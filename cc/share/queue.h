/*
 * Copyright (C) dirlt
 */

#ifndef __CC_COMMO_QUEUE_H__
#define __CC_COMMO_QUEUE_H__

#include <functional>
#include <vector>
#include <queue>
#include "share/lock.h"
#include "share/cond.h"
#include "share/logging.h"

namespace share {

// the followings are MWMR(MultiWrite and MultiRead) thread safe.
// * BlockingPriorityQueue
// * BlockingQueue
// * BlockingDLinkedListQueue
// * BoundedBlockingQueue

// but the SyncedQueue is for MWSR(SingeWrite and SingeRead) or MWMR thread safe.
// depends on the mechanism of cond.wait. if cond.wait return true and can always
// guarantee the next reader can read some thing in many read threads.
// if the Q is for one thread, I think SyncedQueue is enough and much efficient.
// * SyncedQueue templated with(
//    SLinkedListQueue
//    DLinkedListQueue
//    STLQueue
//    STLDeque
//    STLPriorityQueue
// but for most case, we can archive MWMR by call wait(timeout) and poll & poll again.
// so here is some thought about code.
// sometimes we wrote incorrect code, but it's correct in some applicaiton.
// that's enough. we don't need to  write absolute correct code. it costs too much and less efficient.
// relatively correct code is enough for app, for us.it's easy to write and read, and it works.

// 2012-1-12 seems all condition are (MWMR) now:).
// 2012-3-21 I still don't think it's good idea use ScyncedQueue. I think we should choose much more
// stable and well accepted implementation such as using pthread lock and cond.

// ------------------------------------------------------------
// BlockingPriorityQueue Interface.
// highest value comes first.
template < typename T, typename Compare = std::less<T> >
class BlockingPriorityQueue {
public:
    BlockingPriorityQueue():
        mutex_(), notEmpty_(mutex_), pqueue_() {
    }
    void push(const T& x) {
        LockGuard<MutexLock> lock(&mutex_);
        pqueue_.push(x);
        notEmpty_.notify();
    }
    bool pop(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while(pqueue_.empty()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!pqueue_.empty());
        *v = pqueue_.top();
        pqueue_.pop();
        return true;
    }
    bool top(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while(pqueue_.empty()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!pqueue_.empty());
        *v = pqueue_.top();
        return true;
    }
    size_t size() const {
        LockGuard<MutexLock> lock(&mutex_);
        return pqueue_.size();
    }
private:
    mutable MutexLock mutex_;
    Condition notEmpty_;
    std::priority_queue<T, std::vector<T>, Compare> pqueue_;
}; // class BlockingPriorityQueue

// ------------------------------------------------------------
// BlockingQueue Interface.
template<typename T>
class BlockingQueue {
public :
    BlockingQueue() :
        mutex_(), notEmpty_(mutex_), queue_() {
    }
    void push(const T& x) {
        LockGuard<MutexLock> lock(&mutex_);
        queue_.push_back(x);
        notEmpty_.notify();
    }
    void push_front(const T& x) {
        LockGuard<MutexLock> lock(&mutex_);
        queue_.push_front(x);
        notEmpty_.notify();
    }
    bool pop(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while (queue_.empty()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!queue_.empty());
        *v = queue_.front();
        queue_.pop_front();
        return true;
    }
    size_t size() const {
        LockGuard<MutexLock> lock(&mutex_);
        return queue_.size();
    }
private:
    mutable MutexLock mutex_;
    Condition notEmpty_;
    std::deque<T> queue_;
}; // class BlockingQueue

// ------------------------------------------------------------
// BlockingDLinkedListQueue Interface.
// T should be pointer.!!!
// and T has fields 'prev' and 'next whose type is also T.
template< typename T>
class BlockingDLinkedListQueue {
public:
    BlockingDLinkedListQueue():
        mutex_(), notEmpty_(mutex_),
        head_(NULL), tail_(NULL) {
    }
    void push(T item) {
        LockGuard< MutexLock > lock(&mutex_);
        item->next = NULL;
        if(empty_()) {
            head_ = item;
            tail_ = item;
            item->prev = NULL;
        } else {
            tail_->next = item;
            item->prev = tail_;
            tail_ = item;
        }
        notEmpty_.notify();
    }
    void push_front(T item) {
        LockGuard< MutexLock > lock(&mutex_);
        item->prev = NULL;
        if(empty_()) {
            head_ = item;
            tail_ = item;
            item->next = NULL;
        } else {
            item->next = head_;
            head_->prev = item;
            head_ = item;
        }
        notEmpty_.notify();
    }
    bool pop(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while(empty_()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!empty_());
        T x = head_;
        head_ = head_->next;
        if(head_ == NULL) {
            tail_ = NULL;
        } else {
            head_->prev = NULL;
        }
        x->prev = NULL;
        x->next = NULL;
        *v = x;
        return true;
    }
    void clear(T* v) {
        LockGuard<MutexLock> lock(&mutex_);
        *v = head_;
        head_ = NULL;
        tail_ = NULL;
    }
    void replace(T o, T n) {
        LockGuard<MutexLock> lock(&mutex_);
        if(o->prev) {
            o->prev->next = n;
        }
        n->prev = o->prev;
        if(o->next) {
            o->next->prev = n;
        }
        n->next = o->next;
    }
    void remove(T x) {
        LockGuard<MutexLock> lock(&mutex_);
        if(head_ == x &&
                tail_ == x) {
            head_ = NULL;
            tail_ = NULL;
        } else if(head_ == x) {
            head_ = x->next;
            head_->prev = NULL;
        } else if(tail_ == x) {
            tail_ = x->prev;
            tail_->next = NULL;
        } else {
            x->prev->next = x->next;
            x->next->prev = x->prev;
        }
    }
private:
    bool empty_() const {
        if(head_ == tail_ && head_ == NULL) {
            return true;
        }
        return false;
    }
    MutexLock mutex_;
    Condition notEmpty_;
    T head_;
    T tail_;
}; // class BlockingDLinkedListQueue

// ------------------------------------------------------------
// BlockingSLinkedListQueue Interface.
// T should be pointer.!!!
// and T has fields 'prev' and 'next whose type is also T.
template< typename T>
class BlockingSLinkedListQueue {
public:
    BlockingSLinkedListQueue():
        mutex_(), notEmpty_(mutex_),
        head_(NULL), tail_(NULL) {
    }
    void push(T item) {
        LockGuard< MutexLock > lock(&mutex_);
        item->next = NULL;
        if(empty_()) {
            head_ = item;
            tail_ = item;
        } else {
            tail_->next = item;
            tail_ = item;
        }
        notEmpty_.notify();
    }
    void push_front(T item) {
        LockGuard< MutexLock > lock(&mutex_);
        if(empty_()) {
            head_ = item;
            tail_ = item;
            item->next = NULL;
        } else {
            item->next = head_;
            head_ = item;
        }
        notEmpty_.notify();
    }
    bool pop(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while(empty_()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!empty_());
        T x = head_;
        head_ = head_->next;
        if(head_ == NULL) {
            tail_ = NULL;
        }
        x->next = NULL;
        *v = x;
        return true;
    }
    void clear(T* v) {
        LockGuard<MutexLock> lock(&mutex_);
        *v = head_;
        head_ = NULL;
        tail_ = NULL;
    }
private:
    bool empty_() const {
        if(head_ == tail_ && head_ == NULL) {
            return true;
        }
        return false;
    }
    MutexLock mutex_;
    Condition notEmpty_;
    T head_;
    T tail_;
}; // class BlockingSLinkedListQueue

// ------------------------------------------------------------
// BoundedBlockingQueue Interface.
template<typename T>
class BoundedBlockingQueue {
public:
    explicit BoundedBlockingQueue(int max_size):
        mutex_(), notEmpty_(mutex_), notFull_(mutex_), queue_() {
        size_ = max_size;
    }
    bool push(const T& x, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while (queue_.size() == size_) {
            if(wait_ms == -1) {
                notFull_.wait();
            } else {
                if(!notFull_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!(queue_.size() == size_));
        queue_.push_back(x);
        notEmpty_.notify();
        return true;
    }
    bool push_front(const T& x, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while (queue_.size() == size_) {
            if(wait_ms == -1) {
                notFull_.wait();
            } else {
                if(!notFull_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!(queue_.size() == size_));
        queue_.push_front(x);
        notEmpty_.notify();
        return true;
    }
    bool pop(T* v, int wait_ms = -1) {
        LockGuard<MutexLock> lock(&mutex_);
        struct timespec tp;
        if(wait_ms != -1) {
            gettime_timespec(&tp);
            addtime_timespec(&tp, wait_ms);
        }
        while (queue_.empty()) {
            if(wait_ms == -1) {
                notEmpty_.wait();
            } else {
                if(!notEmpty_.timedWait(&tp)) {
                    return false;
                }
            }
        }
        assert(!queue_.empty());
        *v = queue_.front();
        queue_.pop_front();
        notFull_.notify();
        return true;
    }
    size_t size() const {
        LockGuard<MutexLock> lock(&mutex_);
        return queue_.size();
    }
private:
    mutable MutexLock mutex_;
    Condition notEmpty_;
    Condition notFull_;
    std::deque<T> queue_;
    size_t size_;
}; // class BoundedBlockingQueue

// ------------------------------------------------------------
// TODO(dirlt): I don't think the following code is stable and well test!!!
// ------------------------------------------------------------
// SyncedQueue Interface.
// Lock sees 'lock.h'
// Cond sees 'cond.h'
template < typename Q,
         typename T,
         typename Lock,
         typename Cond >
class SyncedQueue {
public:
    static const int kRetryCounter = 10;
    void push(T x) {
        lock_.lock();
        queue_.push(x);
        lock_.unlock();
        cond_.notify();
    }
    void push_front(T x) {
        lock_.lock();
        queue_.push_front(x);
        lock_.unlock();
        cond_.notify();
    }
    bool pop(T* x, int wait_ms = -1) {
        if(!cond_.wait(wait_ms)) {
            return false;
        }
        lock_.lock();
#ifdef DEBUG
        assert(!queue_.empty());
#endif
        if(x) {
            *x = queue_.pop();
        }
        lock_.unlock();
        return true;
    }
    bool top(T* x, int wait_ms = -1) {
        if(!cond_.wait(wait_ms)) {
            return false;
        }
        lock_.lock();
        if(x) {
            *x = queue_.top();
        }
        lock_.unlock();
        cond_.notify(); // notify back.
        return true;
    }
    bool empty() const {
        LockGuard< Lock > lockguard;
        return queue_.empty();
    }
private:
    Q queue_;
    Lock lock_;
    Cond cond_;
}; // class SyncedQueue

// ------------------------------------------------------------
// SLinkedListQueue Inteface.
// T should be pointer!!!
// T has field 'next' whose type is T
template<typename T>
class SLinkedListQueue {
public:
    SLinkedListQueue():
        head_(NULL),
        tail_(NULL) {
    }
    void push(T item) {
        item->next = NULL;
        if(empty()) {
            head_ = item;
            tail_ = item;
        } else {
            tail_->next = item;
            tail_ = item;
        }
    }
    void push_front(T item) {
        if(empty()) {
            head_ = item;
            tail_ = item;
            item->next = NULL;
        } else {
            item->next = head_;
            head_ = item;
        }
    }
    T pop() {
        T x = head_;
        head_ = head_->next;
        if(head_ == NULL) {
            tail_ = NULL;
        }
        x->next = NULL;
        return x;
    }
    bool empty() const {
        if(head_ == tail_ && head_ == NULL) {
            return true;
        }
        return false;
    }
    T head() const {
        return head_;
    }
    T tail() const {
        return tail_;
    }
private:
    T head_;
    T tail_;
}; // class SLinkedListQueue

// ------------------------------------------------------------
// DLinkedListQueue Interface.
// T should be pointer.!!!
// T has field 'prev' and 'next whose type is T
template<typename T>
class DLinkedListQueue {
public:
    DLinkedListQueue():
        head_(NULL),
        tail_(NULL) {
    }
    void push(T item) {
        item->next = NULL;
        if(empty()) {
            head_ = item;
            tail_ = item;
            item->prev = NULL;
        } else {
            tail_->next = item;
            item->prev = tail_;
            tail_ = item;
        }
    }
    void push_front(T item) {
        item->prev = NULL;
        if(empty()) {
            head_ = item;
            tail_ = item;
            item->next = NULL;
        } else {
            item->next = head_;
            head_->prev = item;
            head_ = item;
        }
    }
    T pop() {
        T x = head_;
        head_ = head_->next;
        if(head_ == NULL) {
            tail_ = NULL;
        } else {
            head_->prev = NULL;
        }
        x->prev = NULL;
        x->next = NULL;
        return x;
    }
    void replace(T o, T n) {
        if(o->prev) {
            o->prev->next = n;
        }
        n->prev = o->prev;
        if(o->next) {
            o->next->prev = n;
        }
        n->next = o->next;
    }
    void remove(T x) {
        if(head_ == x &&
                tail_ == x) {
            head_ = NULL;
            tail_ = NULL;
        } else if(head_ == x) {
            head_ = x->next;
            head_->prev = NULL;
        } else if(tail_ == x) {
            tail_ = x->prev;
            tail->next = NULL;
        } else {
            x->prev->next = x->next;
            x->next->prev = x->prev;
        }
    }
    bool empty() const {
        if(head_ == tail_ && head_ == NULL) {
            return true;
        }
        return false;
    }
    T head() const {
        return head_;
    }
    T tail() const {
        return tail_;
    }
private:
    T head_;
    T tail_;
}; // class DLinkedListQueue

// ------------------------------------------------------------
// STLQueue Interface.
template< typename T>
class STLQueue:
    public std::queue<T> {
public:
    typedef std::queue<T> Base;
    T pop() {
        T x = Base::front();
        Base::pop();
        return x;
    }
    T top() {
        return Base::front();
    }
    bool empty() const {
        return Base::empty();
    }
}; // class STLQueue

// ------------------------------------------------------------
// STLDeque Interface.
template< typename T>
class STLDeque :
    public std::deque<T> {
public:
    typedef std::deque<T> Base;
    void push(T x) {
        Base::push_back(x);
    }
    void push_front(T x) {
        Base::push_front(x);
    }
    T pop() {
        T x = Base::front();
        Base::pop_front();
        return x;
    }
    T top() {
        return Base::front();
    }
    bool empty() const {
        return Base::empty();
    }
}; // class STLDeque

// ------------------------------------------------------------
// STLPriorityQueue Interface.
template < typename T, typename Compare = std::less<T> >
class STLPriorityQueue:
    public std::priority_queue<T, std::vector<T>, Compare> {
public:
    typedef std::priority_queue<T, std::vector<T>, Compare> Base;
    void push(T x) {
        DEBUG("STLPriorityQueue push");
        Base::push(x);
    }
    T pop() {
        T x = Base::top();
        Base::pop();
        return x;
    }
    T top() {
        return Base::top();
    }
    bool empty() const {
        return Base::empty();
    }
}; // class STLPriorityQueue

} // namespace share

#endif // __CC_COMMO_QUEUE_H__
