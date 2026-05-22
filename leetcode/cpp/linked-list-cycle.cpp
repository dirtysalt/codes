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
    bool hasCycle(ListNode* head) {
        ListNode *p0 = head, *p1 = head;
        while (p0 != NULL && p1 != NULL) {
            p0 = p0->next;
            p1 = p1->next;
            if (p1 == NULL) {
                return false;
            }
            p1 = p1->next;
            if (p0 == p1) {
                return true;
            }
        }
        return false;
    }
};
