## Method overloading

**method name is the same, but parameter type list is different**
1. different types
2. different num of parameters
3. different order

# Notes

## return type cannot be used to identify which function to use

```java
public class test {
	
	public static int add(double a, double b) {
		return (int) (a + b);
	}
	
	public static double add(double a, double b) {
		return (a + b);
	}
	
	public static void main(String[] args) {
		double a = 1.3, b = 2.4;
//		int c = add(a, b);
		System.out.println(add(a, b));
	}
}

```