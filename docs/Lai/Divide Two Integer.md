1. self intro
	infrastructure engineer in search
	ml infrastructure, inside tools for testing and developments
	service owner for search slogan service
	team search feature - for users and other engineering teams
	drive the team of search quality - responsible
	organize and manage the developments and teams - details
	
	impact, complexity for what you have done technically!!
	millions level users and high qps, autoscaling and analysis
tech stacks - details


2. Why do you want to change your company?
	food truck search problem
	没听清楚 → double check

3. What is the biggest bug/mistake you have committed in your work?
	broken for the owned service
		details - main service -> microservice, parameters
			- coordination of the dependency of push process 
for different time zone
-
	Why - deep analysis
	What - 

	3.1 how do you solve the problem
		- oncall wake up 2AM
		- push and rollback in time
	3.2 what do you learnt and what to do in the future
		- use the centralized timezone
		- how do you enforce? What are the actions?
			- change the whole process, share calendar, ping on slack and calendar, link on other events, mark and account for the completeness
		- work and cooperate with diverse working environment
			- proactively communication


Literal point 0

insight point 1  - why your interviewer asked this question? Passion to join company?

insight point 2 - think about in depth what he wants to know? What can you bring to our company?


转专业的问为啥转码应该怎么回答 ??

insight point 1 - passion + motivation ⇒ 

100 / 3  
100 -3-3-3-3-3 ….. 

10^10 / 1


Given two int value a and b, find a/b
Notice: you can not use "/" operation.

4 / 3 = 1 --- 1

4 / 3 = 1

x * 3 = closet number to 4 but smaller than 4


< 0 sign 1 or both > 0 sign 1, -1
Math.abs(a) Math.abs(b)

if (a == 0) {
	return 0;
}

min = 1, max = dividend
mid = (max - min) / 2 + min
mid * divisor = number > dividend 
max = mid;
mid * divisor = number < dividend
min = mid + 1
until we make min == max
min will be the closest we can and smaller than dividend

dividend = 4, divsior = 3

min = 1, max = 4

mid = (4 - 1) >> 1 + min = 2;

number = 2 * 3 = 6 > 4
max = mid = 2

min = 1, max = 2
mid = 1
number = 1 * 3 = 3 < 4
min = mid + 1 = 2;
min = 2, max = 2

we get result as 2
we check 2, 2 * 3 = 6
we will return 2 - 1 = 1

min = mid
max = mid - 1

min =1 , max  = 4
mid = 2
max = 2 - 1
min = 1, max = 1

public int divide(int dividend, int divisor) {
	if (divisior == 0) {
		throw new Exception(“divisor cannot be 0”);
}
if (dividend == 0 || dividend < divisor) {
	return 0;
}
	int min = 1, max = dividend;
	while (min < max) { // when min equals max, end it
		int mid = (max - min) >> 1 + min; // get mid value
		int number = mid * divisor; // calculate possible value
		if (number == dividend) { // we find it, so we directly return it
	return mid;
} else if (number > dividend) { // it looks 
	max = mid - 1;
} else {
	min = mid;
}
}
return min;
}

dividend = 10, divisor = 5

min = 1, max = 10

mid = 5
5 * 5 = 25 > 10

min = 1, max = 4
mid = 2
5 * 2 = 10 = 10
return 2

dividend = 4, divisor = 3

dividend = 0
return 0

divisor = 0
throw out of exception


1 / 2
dividend < divisor 0 

dividend = 11 divisor = 3

min: 1 max: 11
mid = 6 * 3 = 18 > 11

min: 1 max: 5
mid = 3 * 3 = 9 < 11
min: 3 max: 5
mid = 4 * 3 = 12 > 11
min: 3  max: 3
mid = 3 * 3 = 9 < 11
mi

1 -- dividend
log(dividend)
O(1)

in the worst case, 1  2 ^ 32  ---> 2^31 ---> 


10^10 / 10^9  = 10                   1 0 1 0

search range - [1, 2^4]

min: 1 to max: 10^10

log(a/b) = loga - logb


Clarification & Assumptions:
	b = 0? Why throw an exception in this case? - this is runtime error
		NullPointerException
		ArrayIndexOutOfBoundException
IlegalArumentException
IlegalStateException
ArithmeticException	("divisor can not be 0")

	types of a,b - int, overflow?  the result will never overflow?
		MIN_VALUE = -2^31
		MAX_VALUE = 2^31 - 1
		MIN_VALUE / -1 = ?
	What is the result type? int
	positive/negative for a,b?
		-7 / 4 = -1  or   -2

Result:
	Binary Search Application
	动手过例子，---> 
1. 逻辑的关键部分 整理清楚 各种case，物理意义，  
2. 解释你的high level，detail的逻辑
           4 / 3
            1       2       3       4
         3          6      9         12
          min    mid                  max 
                   2*3 =6
         min,max
      
	high level - 为什么能用binary search
把Binary Search的要点讲清楚
		1. search range → [min, max]
		2. search range reduce size each round → while loop()能进得去和跳的出来
	
                  [1,       2]
                   min  max
                   mid  

  case 1    max = mid - 1
  case 2    min = mid

	
Test 
	cover all possible code branches



10 / 3 =  3