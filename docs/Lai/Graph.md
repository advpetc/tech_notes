## Tree vs Graph

1. Graph can have cycle while tree cannot
2. Graph can be **not** connected, which tree cannot

## Analyze Time Complexiy

G = V + E

V: vertex, E: edge

min edge = 0 (not connected)

max edge = $V^2$ (each vertex can connect to all the other in directed graph)

$O(N) = O(V^2)$

## DFS vs BFS: space less than BFS

1.5 Given an input array with integers, how to split the array into k subarray, such that each subarray shares the same sum.
e.g. input[N] = {3,-1,4,6,-8,1,1}, and k = 3
     output = {3,-1} {4,6,-8} {1,1} with all sum is equal to two



1.6 Given an input array with integers, how to split the array into k subarrays (subarray may NOT be adjacent to each other), such that each subarray shares the same sum

E.g. input[N] = { 3 -1,1 1 1 2 2 2  4, 6, -8, 1, 1 }. and k == 3.
Output =  {3,-1}   {4, 6, - 8}  {1, 1}  which all have a sum that is equal to two.