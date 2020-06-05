# Java pass-by-value

1. reassignment

```java
int[] a = new int[]{1}; // a is on stack
int[] b = a; // b still store on stack
b = new int[]{2};
// if print a, it will output 1
```

![Screen Shot 2020-05-10 at 8.03.06 PM.png](resources/1FFE01BC74499722A93728CFE1216FF9.png =269x342)

```java
int[] a = new int[]{1}; // a is on stack
int[] b = a; // b still store on stack
b[0] = 2;
// if print a, it will output 2
```

2. pass in as parameter

```java
// anything "new" in function will stay local and will not modify the outter scope variable
public void reassign(int[] array) {
	array = new int[]{2};
}

public void modify(int[] array) {
	array[0] = 2;
}

public int[] returnArray(int[] array) {
	array = new int[]{2};
	return array;
}

public void foo(int[] array) {
	array[0] = 2; // output this value 2
	array = new int[]{3};
	array[0] = 4;
}

public void foo2(int[] array) {
	array[0] = 2;
	array[0] = 4; // output 4
	array = new int[]{3};
}

public static void main(String[] args) {
	int[] array = new int[]{1};
	reassign(array); //what’s the result? 1
	modify(array); //what’s the result? 2 (ignore previous statement)
	array = returnArray(array); //what’s the result? 2 (ignore previous statement)
}
   

```

![reassign](resources/4ED71DE6EF426984675E837603275C6C.png =226x265)

![modify](resources/69DA2A1E9F25BB841C2D2DDF98048A70.png =212x238)

## debug

```java
public class Solution {
 public void reverse(int[] array) {
   int[] array1 = new int[array.length];
   for (int i=0; i<array.length; i=i+1) {
    array1[i]=array[array.length-1-i];
   }
   array = array1; // Write your solution here
 }

```

Problem: Give an array list of integer, calculate the sum of squares of all its elements.
Note: return 0 if the list is null or empty.
 
Example:
list = {1,2,3} → returns 14 (14=1*1+2*2+3*3)

```java
public class Solution {
 public int sumOfSquare(List<Integer> list) {
    if (list == null || list.isEmpty()) {
	  return 0;
    }
    int sum = 0;
    for (int i = 0; i < list.size(); i++) {
    	sum += list.get(i) * list.get(i);
    }
    return sum;
}
```

# Misc

1. String s = 4 + "aa"; // will print 4aa, because 4.toString() + "aa", however it won't work in c++
2. low -> high precision: will cast implicitly (no need to add (long) for example).
3. high -> low precision: need explict cast