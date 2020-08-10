## Closest Number In Binary Search Tree

In a binary search tree, find k nodes containing the closest numbers to the given target number. return them in sorted array

Assumptions:

The given root is not null.
There are no duplicate keys in the binary search tree.
Examples:
```
    5

  /    \

2      11

     /    \

    6     14
```
closest number to 4 is 5

closest number to 10 is 11

closest number to 6 is 6

How is the binary tree represented?

We use the level order traversal sequence with a special symbol "#" denoting the null node.

For Example:

The sequence [1, 2, 3, #, #, 4] represents the following binary tree:
```
    1

  /   \

 2     3

      /

    4
```

### Analysis

Because it is a binary search tree, if we do in order traversal, then we can get the sequence in ascending order. Imagine we have a sliding window (implemented as a queue), and we keep pushing in the element whose absolute value with target is less than current top's absolute value. 

### Code

```java
/**
 * public class TreeNode {
 *   public int key;
 *   public TreeNode left;
 *   public TreeNode right;
 *   public TreeNode(int key) {
 *     this.key = key;
 *   }
 * }
 */
public class Solution {
  private void helper(TreeNode node, double target, int k, Queue<Integer> queue) {
    if (node == null)
      return;

    helper(node.left, target, k, queue); // in order traverse the left
    if (queue.size() < k) // window isn't full yet
      queue.offer(node.key);
    else {
      // use current node as the right end of the sliding window
      if (Math.abs(target - node.key) < Math.abs(target - queue.peek())) {
        queue.poll();
        queue.offer(node.key)
      } else // not use current node
        return;
    }
    helper(node.right, target, k, queue); // in order traverse the right
  }
  public int[] closestKValues(TreeNode root, double target, int k) {
    if (k <= 0)
      return new int[0];

    Queue<Integer> queue = new ArrayDeque<>(k); // sliding window
    helper(root, target, k, queue);
    int[] result = new int[queue.size()];
    for (int i = 0; i < result.length; i++)
      result[i] = queue.poll();

    return result;
  }
}

```