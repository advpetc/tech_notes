# Recursion and Tree

## Is tree symmetric

![Screen Shot 2020-05-12 at 3.31.27 PM.png](resources/30BFA1DEDAEC5089DDEDD12ED1EF379D.png)

### Recurison Tree

![Screen Shot 2020-05-12 at 3.32.11 PM.png](resources/696E8DE4BA0667EC6199D5EB8444EC61.png)

### Solution

```c
bool isSymmetric(left, right)
  if left == null and right == null
    return true
  else if left == null || right == null
    return false
  else if left.val != right.val
    return false
  else
    return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
```

Time = O(n/2)=O(n)

## Calculate Time Complexity

Branch Factor: b
Height: h

Total Complexity: $b^h$



