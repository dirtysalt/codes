/* coding:utf-8
 * Copyright (C) dirlt
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <cstdio>
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

class Solution {
   public:
    bool match(TreeNode* s, TreeNode* t) {
        if (s == NULL && t == NULL) return true;
        if (s == NULL || t == NULL) return false;
        return (s->val == t->val) && match(s->left, t->left) &&
               match(s->right, t->right);
    }

    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (t == NULL && s == NULL) return true;
        if (t == NULL || s == NULL) return false;
        if (match(s, t)) return true;
        return isSubtree(s->left, t) || isSubtree(s->right, t);
    }
};
