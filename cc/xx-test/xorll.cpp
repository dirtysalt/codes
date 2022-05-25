/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <cstdio>
#include <cstdint>

struct Node {
    int value;
    void *ptr;
};

#define XOR_PTR(a, b) (void *)(((uintptr_t)a) ^ ((uintptr_t)b))
#define XOR_NODE(a, b) (struct Node *)(((uintptr_t)a) ^ ((uintptr_t)b))
#define DEBUG(fmt, ...)                      \
    do {                                     \
        fprintf(stderr, fmt, ##__VA_ARGS__); \
    } while (0)

#define WALK_DIR_HEAD_TO_TAIL 0
#define WALK_DIR_TAIL_TO_HEAD 1
#define OP_DIR_RIGHT 0
#define OP_DIR_LEFT 1

struct LL {
    struct Node head;
    struct Node tail;
    int num;
};

void init_ll(LL *ll) {
    ll->head.ptr = XOR_PTR(0, &(ll->tail));
    ll->tail.ptr = XOR_PTR(&(ll->head), 0);
    ll->num = 0;
}

void walk(LL *ll, int walk_dir, int (*cb)(Node *, void *), void *arg) {
    assert((walk_dir == WALK_DIR_HEAD_TO_TAIL) || (walk_dir == WALK_DIR_TAIL_TO_HEAD));
    struct Node *pp = &(ll->head);
    struct Node *end = &(ll->tail);
    if (walk_dir == WALK_DIR_TAIL_TO_HEAD) {
        pp = &(ll->tail);
        end = &(ll->head);
    }

    struct Node *p = XOR_NODE(0, pp->ptr);
    while (p != end) {
        int ret = cb(p, arg);
        if (ret != 0) {
            break;
        }
        struct Node *next = XOR_NODE(pp, p->ptr);
        pp = p;
        p = next;
    }
}

void push(LL *ll, struct Node *node, int op_dir) {
    assert((op_dir == OP_DIR_LEFT) || (op_dir == OP_DIR_RIGHT));
    struct Node *tail = &(ll->tail);
    if (op_dir == OP_DIR_LEFT) {
        tail = &(ll->head);
    }

    struct Node *p = XOR_NODE(tail->ptr, 0);
    void *v = XOR_PTR(p->ptr, tail);
    p->ptr = XOR_PTR(v, node);
    node->ptr = XOR_PTR(p, tail);
    tail->ptr = XOR_PTR(node, 0);
    ll->num++;
}

struct Node *pop(LL *ll, int op_dir) {
    assert((op_dir == OP_DIR_LEFT) || (op_dir == OP_DIR_RIGHT));
    struct Node *tail = &(ll->tail);
    struct Node *end = &(ll->head);
    if (op_dir == OP_DIR_LEFT) {
        tail = &(ll->head);
        end = &(ll->tail);
    }

    struct Node *p = XOR_NODE(tail->ptr, 0);
    if (p == end) {
        return NULL;
    }
    struct Node *pp = XOR_NODE(p->ptr, tail);
    void *v = XOR_PTR(pp->ptr, p);
    pp->ptr = XOR_PTR(v, tail);
    tail->ptr = XOR_PTR(pp, 0);
    ll->num--;
    return p;
}

int print_node(Node *p, void *arg) {
    int *control = (int *)arg;
    if ((*control & 0x1) == 0) {
        *control |= 0x1;
    } else {
        printf(", ");
    }
    printf("%d", p->value);
    return 0;
}

void print_ll(LL *ll, int walk_dir, const char *msg) {
    printf("%s\n", msg);
    printf("size = %d, contents = [", ll->num);
    int control = 0;
    walk(ll, walk_dir, print_node, &control);
    printf("]\n");
}

void test() {
    LL ll;
    const int n = 10;
    struct Node nodes[n];
    for (int i = 0; i < n; i++) {
        nodes[i].value = i;
    }
    init_ll(&ll);
    for (int i = 0; i < n; i++) {
        push(&ll, nodes + i, OP_DIR_RIGHT);
    }
    print_ll(&ll, WALK_DIR_TAIL_TO_HEAD, "walk ll: tail to head");
    print_ll(&ll, WALK_DIR_HEAD_TO_TAIL, "walk ll: head to tail");

    const int m = 3;
    for(int i= 0;i<m;i++) {
        pop(&ll, OP_DIR_RIGHT);
        pop(&ll, OP_DIR_LEFT);
    }
    print_ll(&ll, WALK_DIR_TAIL_TO_HEAD, "walk ll: tail to head");
    print_ll(&ll, WALK_DIR_HEAD_TO_TAIL, "walk ll: head to tail");
}

int main() {
    test();
    return 0;
}
