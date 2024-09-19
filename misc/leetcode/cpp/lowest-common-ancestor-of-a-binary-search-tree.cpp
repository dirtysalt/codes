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

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

class Solution {
   public:
    TreeNode* find(TreeNode* root, TreeNode* p, TreeNode* q) {
        if ((root == p) || (root == q)) return root;
        if (root->val >= p->val and root->val < q->val) return root;
        if (root->val < p->val) return find(root->right, p, q);
        return find(root->left, p, q);
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) {
            return find(root, q, p);
        }
        return find(root, p, q);
    }
};
