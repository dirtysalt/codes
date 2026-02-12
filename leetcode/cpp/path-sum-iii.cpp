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
    TreeNode *left, *right;
};
class Solution {
   public:
    int trace(TreeNode* root, int exp) {
        if (root == NULL) {
            return 0;
        }
        int count = 0;
        if (root->val == exp) {
            count += 1;
        }
        count += trace(root->left, exp - root->val);
        count += trace(root->right, exp - root->val);
        return count;
    }
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        int count = 0;
        count += trace(root, sum);
        count += pathSum(root->left, sum);
        count += pathSum(root->right, sum);
        return count;
    }
};
