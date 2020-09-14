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
    bool hasPathSum(TreeNode* root, int sum) {
        // safe guard
        if (root == NULL) return false;
        // leaf node.
        if (root->left == NULL && root->right == NULL) {
            return root->val == sum;
        }
        return hasPathSum(root->left, sum - root->val) ||
               hasPathSum(root->right, sum - root->val);
    }
};
