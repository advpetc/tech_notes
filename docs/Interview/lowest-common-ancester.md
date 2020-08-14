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

## Variant 3: TreeNode has a parent pointer

这个题目分析一下可以看出和树并没有什么关系，我们把parent指针看成next，这个题目就变成了给你两条链表，返回他们的交点，若没有返回null

所以，我们其实不需要去计算他们到交点的高度差，我们把这两个节点成为a和b，交点称为i，链表结尾称为e，可以发现，两条链表的长度差就是i到a和b的长度差，所以当走到末尾时，我们让他从另一个链表的头部开始继续遍历，只要有交点，他们一定会碰在一起

changeOne 和 changeTwo 在这里使得只会走一次，避免没有相交时进去死循环

### Code 1

```java
/**
 * public class TreeNodeP {
 *   public int key;
 *   public TreeNodeP left;
 *   public TreeNodeP right;
 *   public TreeNodeP parent;
 *   public TreeNodeP(int key, TreeNodeP parent) {
 *     this.key = key;
 *     this.parent = parent;
 *   }
 * }
 */
public class Solution {
  public TreeNodeP lowestCommonAncestor(TreeNodeP one, TreeNodeP two) {
    if(one == null || two == null){
      return null;
    }
    TreeNodeP oneCurr = one;
    TreeNodeP twoCurr = two;
    boolean changeOne = false, changeTwo = false;

    while(oneCurr != null && twoCurr != null && oneCurr != twoCurr){
      oneCurr = oneCurr.parent; // keep going up
      twoCurr = twoCurr.parent;

      if(oneCurr == twoCurr){ // terminate if meet up
        return oneCurr;
      }

      if(oneCurr == null && changeOne == false){ // only alternate once
        oneCurr = two; // finish oneCurr, now start with two's head
        changeOne = true;
      }
      if(twoCurr == null && changeTwo == false){ // only alternate once
        twoCurr = one;
        changeTwo = true;
      }
    }
    if(oneCurr == twoCurr){ // possible that after the for loop they meet
      return oneCurr;
    }
    return null;
  }
}
```

### Code 2: check height and decide which node to proceed up

```c
#include <bits/stdc++.h>

using namespace std;

class TreeNodeP {
 public:
  int value;
  TreeNodeP* left;
  TreeNodeP* right;
  TreeNodeP* parent;
  TreeNodeP(int v, TreeNodeP* p)
      : value(v), left(NULL), right(NULL), parent(p) {}
};

class Solution {
 public:
     int height(TreeNodeP* node) {
         int cnt = 0;
         while (node) {
             cnt++;
             node = node -> parent;
         }
         return cnt;
     }

  TreeNodeP* solve(TreeNodeP* one, TreeNodeP* two) {
    if (one == two) return one;
    if (!one || !two) return NULL;
    TreeNodeP* res;
    int h1 = height(one), h2 = height(two);
    if (h1 > h2) {	    	
    	    if ((res = solve(one->parent, two))) return res;
    } else if (h1 < h2) {    	
	    if ((res = solve(one, two->parent))) return res;
    }
    return solve(one->parent, two->parent);
  }
};

int main() {
  TreeNodeP *p1 = new TreeNodeP(5, NULL);
  TreeNodeP *p2 = new TreeNodeP(9, p1);
  TreeNodeP *p3 = new TreeNodeP(12, p1);
  TreeNodeP *p4 = new TreeNodeP(2, p2);
  TreeNodeP *p5 = new TreeNodeP(3, p2);
  TreeNodeP *p6 = new TreeNodeP(14, p3);

  p1 -> left = p2;
  p1 -> right = p3;

  p2 -> left = p4;
  p2 -> right = p5;

  p3 -> right = p6;

  Solution s;
  // TreeNodeP *tmp = new TreeNodeP(-1, NULL);
  cout << s.solve(p5, p2) -> value;
  return 0;
}
```

## Variant 4: find LCA for multiple nodes in the Binary Tree

Use the same logic: find then check if use root as lca.

Physical Meaning of `lca(TreeNode* curr, unordered_set<TreeNode*> st)`:
1. if all the nodes are under curr, return LCA of these nodes.
2. if a subset of the given node are under the root, return LCA of the nodes under root.
3. if none of the nodes are under root, return null.

### Code

```c
class Solution {
 public:
  TreeNode* lca(TreeNode* curr, unordered_set<TreeNode*> st) {
    if (!curr || st.count(curr)) return curr;
    TreeNode* left = lca(curr -> left, st); // if left is under root
    TreeNode* right = lca(curr -> right, st); // if right is under root
    if (left && right) return curr;
    return left ? left : right;
  }
  TreeNode* solve(TreeNode* root, vector<TreeNode*> nodes) {
    unordered_set<TreeNode*> st(nodes.begin(), nodes.end());
    return lca(root, st);
  }
};

```

## Variant 5: find LCA for two nodes for m-ary tree

Use the same logic to find the two corresponding nodes from the binary tree, and then check if any *two* are sharing with the same root. If so, return the root, or return the one that isn't null.

### Code

```java
public class Solution {

  public KnaryTreeNode lowestCommonAncestor(KnaryTreeNode root, KnaryTreeNode a, KnaryTreeNode b) {
    if (root == null || root == a || root == b) return root;
    KnaryTreeNode found = null; // at least two children are found, or just return the one that is found or just null
    for (KnaryTreeNode node : root.children) {
      KnaryTreeNode curr = lowestCommonAncestor(node, a, b);
      if (curr == null) continue;
      if (found != null) return root; // already two nodes are sharing with the current root
      if (found == null) found = curr;
    }
    return found;
  }
}
```

## Variant 6: find LCA for n nodes for m-ary tree

Use the same logic to find the two corresponding nodes from the m-ary tree, and then check if any *two* are sharing with the same root. If so, return the root, or return the one that isn't null.

In the base case, we only need to check if current searched node is one of the node in the set. We don't need to care about duplication, since, all the children of the current node are distinct, meaning if there are *two nodes* being found from the recursion call, we can guarantee that these two nodes are distint.

### Code

```java
/**
* public class KnaryTreeNode {
 *     int key;
 *     List<KnaryTreeNode> children;
 *     public KnaryTreeNode(int key) {
 *         this.key = key;
 *         this.children = new ArrayList<>();
 *     }
 * }
 */
public class Solution {
  KnaryTreeNode helper(KnaryTreeNode root, Set<KnaryTreeNode> set) {
    if (root == null || set.contains(root)) return root;
    KnaryTreeNode found = null;
    for (KnaryTreeNode nei : root.children) {
      KnaryTreeNode node = helper(nei, set);
      if (node == null) continue;
      if (found == null) found = node;
      else return root; 
    }
    return found;
  }

  public KnaryTreeNode lowestCommonAncestor(KnaryTreeNode root, List<KnaryTreeNode> nodes) {
    // Write your solution here
    Set<KnaryTreeNode> set = new HashSet<KnaryTreeNode>(nodes);
    return helper(root, set);
  }
}
```