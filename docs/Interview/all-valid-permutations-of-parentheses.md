# All Vaid Permutation of Parentheses

Get all valid permutations of l pairs of (), m pairs of <> and n pairs of {}, subject to the priority restriction: {} higher than <> higher than ().



Assumptions

    l, m, n >= 0
    
    l + m + n >= 0



Examples

    l = 1, m = 1, n = 0, all the valid permutations are ["()<>", "<()>", "<>()"].
    
    l = 2, m = 0, n = 1, all the valid permutations are [“()(){}”, “(){()}”, “(){}()”, “{()()}”, “{()}()”, “{}()()”].

## Analysis

Use a stack to preserve the priority (lower index means lower priority, and higher priority parenthese should surround the lower priority parenthese).

+ check if is open parenthese
  - if yes, check if is enclosed by higher priority (or empty) and push into the stack
  - if no, check if previous one is the corresponding open parenthese and delete the previous open parenthese index from stack

## Java Code

```java
public class Solution {
  private static final char[] PS = new char[]{'(', ')', '<', '>', '{', '}'};
  public List<String> validParenthesesIII(int l, int m, int n) {
    int[] remain = new int[]{l, l, m, m, n, n};
    int targetLen = 2 * l + 2 * m + 2 * n;
    StringBuilder cur = new StringBuilder();
    Deque<Integer> stack = new LinkedList<Integer>();
    List<String> result = new ArrayList<String>();
    helper(cur, stack, remain, targetLen, result);
    return result;
  }

  private void helper(StringBuilder cur, Deque<Integer> stack, int[] remain,
                      int targetLen, List<String> result) {
    // need to use all parentheses
    if (cur.length() == targetLen) {
      result.add(cur.toString());
      return;
    }
    for (int i = 0; i < remain.length; ++i) {
      if (i % 2 == 0) { // ( < or {
        // top of stack has a lower priority -> need to be surrounded by higher priority parenthese
        if (remain[i] > 0 && (stack.isEmpty() || stack.peekFirst() > i)) { 
          cur.append(PS[i]);
          stack.offerFirst(i);
          remain[i]--;
          helper(cur, stack, remain, targetLen, result);
          cur.deleteCharAt(cur.length() - 1);
          stack.pollFirst();
          remain[i]++;
        }
      } else { // ) > or }
        // only update the cur if previous / top of the stack is the corresponding open parentheses
        if (!stack.isEmpty() && stack.peekFirst() == i - 1) {
          cur.append(PS[i]);
          stack.pollFirst();
          remain[i]--;
          helper(cur, stack, remain, targetLen, result);
          cur.deleteCharAt(cur.length() - 1);
          stack.offerFirst(i - 1);
          remain[i]++;
        }
      }
    }
  }
}

```