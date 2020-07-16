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