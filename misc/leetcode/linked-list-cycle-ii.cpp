/* coding:utf-8
 * Copyright (C) dirlt
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <cstdio>
struct ListNode {
    ListNode* next;
};

class Solution {
   public:
    ListNode* detectCycle(ListNode* head) {
        ListNode *p0 = head, *p1 = head;
        bool cycle = false;
        while (p0 != NULL && p1 != NULL) {
            p0 = p0->next;
            p1 = p1->next;
            if (p1 == NULL) {
                return NULL;
            }
            p1 = p1->next;
            if (p0 == p1) {
                cycle = true;
                break;
            }
        }
        if (!cycle) {
            return NULL;
        }
        p0 = head;
        while (p0 != p1) {
            p0 = p0->next;
            p1 = p1->next;
        }
        return p1;  // or p0
    }
};
