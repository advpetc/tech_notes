## Min and Max value

int: Integer.MAX_VALUE ($2^{31} - 1$), Integer.MIN_VALUE ($-2^{31}$)

## Data structure

### Stack

```java
Deque<Integer> stack = new LinkedList<Integer>();

stack.isEmpty() 
stack.peekFirst()
stack.pollFirst();
stack.offerFirst(1);
```

### String

```java
StringBuilder cur = new StringBuilder();
cur.append('(');
cur.deleteCharAt(cur.length() - 1); // remove last char from the string
String result = cur.toString();
```