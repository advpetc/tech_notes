## Balanced Tree

Def: height of the left and right subtrees of **every node** differ by 1 or less.

### Method 1: check is balanced

```c
int height(TreeNode* root) {
    if (!root) return 0;
    return max(height(root -> left), height(root -> right)) + 1;
}

bool isBalanced(TreeNode* root) {
    if (!root) return true;
    if(abs(height(root -> left) - height(root -> right)) > 1) return false;
    return isBalanced(root -> left) && isBalanced(root -> right);
}
```

#### Analysis

Time: worst case happens when tree is balanced, so there are log(n) levels. first level requires n ops to get height, second = n/2, ....1. So total complexity is $n + n / 2 + n / 4 + .... + n \times 2^{\log{n}} = n \log{n}$
Space: $\log{n}$

### Method 2: check is balanced

```c
int checkDepth(TreeNode* root) {
    if (!root)
        return 0;
    int left = checkDepth(root -> left);
    if (left == -1)
        return -1;
    int right = checkDepth(root -> right);
    if (right == -1)
        return -1;
    if (abs(right - left) > 1)
        return -1;
    else
        return 1 + max(left, right);
}
bool isBalanced(TreeNode* root) {
    if (checkDepth(root) == -1)
        return false;
    else
        return true;
}
```

#### Analysis

For each node, early terminate if left or right subtree is invalid. Each node only requries to visit once, so the time compleixty is $O(n)$
Space Compleixty: the worst case would be like a linkedlist and the height is n, so $O(n)$

## Symmetric Tree

  Assume if we tweak the lchild with rchild of an arbitrary node in a binary tree, then the "structure" of the tree are not changed. Then how can we determinte whether two binary trees' structures are identical.

```c
 bool isTweakedIdentical(TreeNode* l, TreeNode* r) {
    // write your solution here
    if (!l && !r) return true;
    if (!l || !r) return false;
    if (l -> value != r -> value) return false;
    return (isTweakedIdentical(l -> left, r -> right) && isTweakedIdentical(l -> right, r -> left)) ||
           (isTweakedIdentical(l -> right, r -> right) && isTweakedIdentical(l -> left, r -> left)) ||
           (isTweakedIdentical(l -> left, r -> left) && isTweakedIdentical(l -> right, r -> right)) ||
           (isTweakedIdentical(l -> right, r -> left) && isTweakedIdentical(l -> left, r -> right));
  }
```

#### Analysis

Each level has four nodes, and total cost is N. There are $\log_2{N}$ because the wrost case is when the tree is balanced (there are not a lot early terminations). Total number of nodes in the quadral tree is $1 + 4 + 16 .... + 4^{\log_2{n}} \approx 4^{\log_2{n}} = 2^{2\log_2{n}} = 2^{\log_2{n^2}} = O(n^2)$

Space: wrost case is linkedlist so $O(n)$

## Traverse Tree

- pre-order: root -> left -> right
- in-order: left -> root -> right
- post-order: left -> right -> root

### Pre-order

**recursion:**

```c
vector<int> res;
vector<int> preorderTraversal(TreeNode* root) {
    if (!root) return {};
    res.push_back(root -> val);
    preorderTraversal(root -> left);
    preorderTraversal(root -> right);
    /* traverse a graph
    for (int i = 0; i < n; ++i) preorder(root -> neighbour[i]);
    */
    return res;
}
```

**iterative:**

```c
vector<int> preorderTraversal(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    stack<TreeNode*> st{{root}};
    while (!st.empty()) {
        TreeNode* t = st.top();
        st.pop();
        res.push_back(t -> val);
        /* traverse a graph
        for (int i = n - 1; i >= 0; --i) preorder(root -> neighbour[i]);
        */
        if (t -> right) st.push(t -> right); // push right first, so it will be popped last
        if (t -> left) st.push(t -> left);
    }
    return res;
}
```

### In-order

**recursion:**

```c
vector<int> res;
vector<int> inorderTraversal(TreeNode* root) {
    if (!root) return {};
    /* traverse a graph: all from 0 to current root
    for (int i = 0; i < m; ++i) inorder(root -> neighbour[i]);
    */
    inorderTraversal(root -> left);
    res.push_back(root -> val);
    /* traverse a graph: all from current root to the end
    for (int i = m; i < n; ++i) inorder(root -> neighbour[i]);
    */
    inorderTraversal(root -> right);
    return res;
}
```

**iterative:**

```c
 vector<int> inorderTraversal(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    stack<TreeNode*> st;
    while (root || !st.empty()) {
        while (root) { // first push all the left children to the stack
            st.push(root);
            root = root -> left;
        }
        root = st.top();
        st.pop();
        res.push_back(root -> val);
        root = root -> right;
    }
    return res;
}
```

### Post-order

**recursion:**

```c
vector<int> res;
vector<int> postorderTraversal(TreeNode* root) {
    if (!root) return {};
    postorderTraversal(root -> left);
    postorderTraversal(root -> right);
    res.push_back(root -> val);
    return res;
}
```

**iterative:**

```c
 vector<int> postorderTraversal(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    stack<TreeNode*> s;
    while (root || !s.empty()) {
      if (root) {
        s.push(root);
        res.insert(res.begin(), root->val);
        root = root->right;
      } else {
        TreeNode* pleft = s.top();
        s.pop();
        root = pleft->left;
      }
    }
    return res;
 }
```

## Binary Searh Tree

### Query

**find min/max:**

```c
while x.left/x.right != null:
    x = x.left/x.right
return x // if using x.left -> min, x.right -> max
```

### Insertion

```c
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        TreeNode *cur = root;
        while (true) {
            if (cur->val > val) {
                if (!cur->left) {
                    cur->left = new TreeNode(val); 
                    break;
                }
                cur = cur->left;
            } else {
                if (!cur->right) {
                    cur->right = new TreeNode(val); 
                    break;
                }
                cur = cur->right;
            }
        }
        return root;
    }
};
```

### Form the Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a bnary search tree with minimal height.

#### Analysis

In order to have the shortest height, we need to make left subtree and right subtree as close size as possible. To do so, we can recursively find the middle value of the sorted array and then appoints that as the root node (left subtree and right subtree).

#### Code

```c
TreeNode* h(vector<int>& arr, int l, int r) {
  if (l == r) return NULL;
  int mid = (l + r) >> 1;
  TreeNode* n = new TreeNode(arr[mid]);
  n -> left = h(arr, l, mid - 1); // [l, mid) are less than arr[mid]
  n -> right = h(arr, mid + 1, r); // (mid, r] are greater than arr[mid]
  return n;
}

TreeNode* createMinimalBST(vector<int>& arr) {
  return h(arr, 0, arr.size() - 1);
}
```

