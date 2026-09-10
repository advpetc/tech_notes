# 1650. Lowest Common Ancestor of a Binary Tree III

Given two nodes of a binary tree `p` and `q`, return *their lowest common ancestor (LCA)*.

Each node will have a reference to its parent node. The definition for `Node` is below:

```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

According to the **definition** of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow **a node to be a descendant of itself**)."

 

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` exist in the tree.

## Analysis

Since every node carries a pointer straight up to its parent, walking from `p` (or `q`) to the root traces out a path, and this problem reduces exactly to **Intersection of Two Linked Lists** (LeetCode 160): find the first node where the `p -> root` path and the `q -> root` path merge.

The classic trick for that problem works here too, without needing to compute either path's length up front: walk two pointers `a` starting at `p` and `b` starting at `q`, one step at a time. Whenever a pointer runs off the top (hits a null `parent`), redirect it to start over from the *other* node instead of `null`. Because both pointers together cover a combined distance equal to `depth(p) + depth(q)` before they first coincide, this rerouting exactly compensates for the difference in depth between `p` and `q`, so `a` and `b` are guaranteed to meet at the LCA.

* Time: $O(h)$, where $h$ is the height of the tree (bounded by the combined depth of `p` and `q`).
* Space: $O(1)$, since we only keep two pointers, unlike the hash-set approach which needs $O(h)$ space to record one path.

## Code

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node* q) {
        Node* a = p;
        Node* b = q;
        while (a != b) {
            a = a->parent ? a->parent : q;
            b = b->parent ? b->parent : p;
        }
        return a;
    }
};
```
