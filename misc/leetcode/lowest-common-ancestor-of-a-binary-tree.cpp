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
    TreeNode* find(TreeNode* root, TreeNode* p, TreeNode* q, int* covers) {
        if (root == NULL) return NULL;

        int c = 0;
        if ((root == p) || (root == q)) c += 1;

        int c0 = 0, c1 = 0;
        TreeNode* t0 = find(root->left, p, q, &c0);
        if (c0 == 2) {
            *covers = 2;
            return t0;
        }
        TreeNode* t1 = find(root->right, p, q, &c1);
        if (c1 == 2) {
            *covers = 2;
            return t1;
        }
        c += (c0 + c1);
        *covers = c;
        return root;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int covers = 0;
        TreeNode* t = find(root, p, q, &covers);
        return t;
    }
};
