/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

void dfs(TreeNode *node, priority_queue<int, vector<int>, greater<int>> &q) {
    q.push(node->val);
    if (node->left) 
        dfs(node->left, q);
    if (node->right)
        dfs(node->right, q);
}

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int, vector<int>, greater<int>> q;
        dfs(root, q);
        while(--k) {
            q.pop();
        }
        return q.top();
    }
};