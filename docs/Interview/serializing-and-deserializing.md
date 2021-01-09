# Serializing and Deserializing a tree

![Screen Shot 2020-07-30 at 10.41.47 PM.png](resources/270278FF3D98AA578466CD5AEF151C00.png)

Can do in-order + pre-order, in-order + post-porder, but cannot do pre-order + post-order

## Given a binary tree, flatten it to a linkedlist **in-place**

![Screen Shot 2020-09-11 at 8.24.44 PM.png](resources/5ACBBA2A06C977640E1A8769DE6F085A.png)

### Using DFS 

![Screen Shot 2020-09-11 at 9.15.07 PM.png](resources/283D95D8921F6988C2D0F32CE3EAC7D8.png)

### Code

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* prev;
    void flatten(TreeNode* root) {
        if (!root) return;
        flatten (root -> right);
        flatten (root -> left);
        root -> right = prev;
        root -> left = NULL;
        prev = root;
    }
    
};
```

### Using iterative

> https://www.acwing.com/video/1469/

1. if left subtree exists, then insert right children of left subtree to the current root's right.
2. if left subtree doesn't exist, visit right subtree of current root, insert left subtree to current root's right.

### Code

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        while (root) {
            TreeNode* p = root -> left;
            if (p) {
                while (p -> right) {
                    p = p -> right;
                }
                p -> right = root -> right;
                root -> right = root -> left;
                root -> left = nullptr;
            }
            root = root -> right;
        }
    }
    
};
```

## Given a binary tree, flatten it to a **doubly linkedlist**

![Screen Shot 2020-09-11 at 9.17.02 PM.png](resources/DBCD62EC150295E2DBF29B8FE91ED2BC.png)

### Code

```c
TreeNode* helper(Treenode* root, TreeNode* prev, TreeNode* head) {
    if (!root) return ;
    helper(root -> left, prev, head);
    if (!pre) head = root;
    else {
        root -> left = prev;
        prev -> right = root;
    }
    prev = root;
    helper(root -> right, prev, head);
}

TreeNode* flatten(TreeNode* root) {
    helper(root, prev, head);
    return head;
}
```