## Variant 1: input is a BST

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

To utilize the property of BST, we should keep elimate either the right or the left subtree of the input tree:

If p and q are all on the right subtree, that means root -> left is less than the min value of p and q
  -> so we don't need to search the root -> left subtree

If p and q are all on the left subtree, that means root -> right is greater than the max value of p and q
  -> so we don't need to search the root -> right subtree
  
If p is in root -> left subtree and p is in root -> right subtree (order doesn't matter), then we juet need to find the first root that satisfy this situation
  -> return current root

Time: $O(log_2{n})$

### Code

```c
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    while (1) {
        if (root -> val < min(p -> val, q -> val))
            root = root -> right;
        else if (root -> val > max(p -> val, q -> val))
            root = root -> left;
        else
            break;
    }
    return root;
}
```

## Variant 2: input is a binary tree

If the two nodes are all existed in the binary tree, then if we start from the root of the tree
1. if find `one` -> `two` is somewhere deeper than `one`, so `one` is the LCA
2. if find `two` -> `one` is somewhere deeper than `two`, so `two` is the LCA


Now the problem reduced to how to find the two nodes from the binay tree.

Time: $O(n)$
Stack Space: $O(height)$

### Code

```c
class Solution {
 public:
  TreeNode* solve(TreeNode* root, TreeNode* one, TreeNode* two) {
    if (!root || root == one || two == root) return root;
    TreeNode* left = solve(root -> left, one, two);
    TreeNode* right = solve(root -> right, one, two);
    if (left && right) return root; // both exist, so current root is the LCA
    return left ? left : right; // return the one that is found
  }
};
```