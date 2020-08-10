Given an integer k, arrange the sequence of integers [1, 1, 2, 2, 3, 3, ...., k - 1, k - 1, k, k], such that the output integer array satisfy this condition:

Between each two i's, they are exactly i integers (for example: between the two 1s, there is one number, between the two 2's there are two numbers).

If there does not exist such sequence, return null.

Assumptions:

k is guaranteed to be > 0
Examples:

k = 3, The output = { 2, 3, 1, 2, 1, 3 }.

## Analysis

The problem can reduce to how to place each element from [1 to k], among all the permutation, find the correct one(s).

## Code

```java
public static class Solution {
		public int[] keepDistance(int k) {
			int[] res = new int[2 * k];
			int[] used = new int[k + 1];
			return helper(res, 0, used) ? res : null;
		}

		private boolean helper(int[] res, int idx, int[] used) {
			if (idx == res.length) return true;
			for (int i = 1; i < used.length; ++i) {
				if (used[i] == 0 || (used[i] == 1 && idx > i && res[idx - i - 1] == i)) {
					res[idx] = i;
					used[i]++;
					if (helper(res, idx + 1, used)) return true;
					used[i]--;
				}
			}
			return false;
		}

	}
```