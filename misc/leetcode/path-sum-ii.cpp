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
#include <vector>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left, *right;
};

class Solution {
   public:
    void trace(TreeNode* root, int sum, vector<int>& stage,
               vector<vector<int>>& paths) {
        if (root == NULL) return;
        if (root->left == NULL && root->right == NULL && root->val == sum) {
            stage.push_back(root->val);
            paths.push_back(stage);
            stage.pop_back();
            return;
        }
        stage.push_back(root->val);
        trace(root->left, sum - root->val, stage, paths);
        trace(root->right, sum - root->val, stage, paths);
        stage.pop_back();
    }
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> paths;
        vector<int> stage;
        trace(root, sum, stage, paths);
        return paths;
    }
};
