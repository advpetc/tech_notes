# Minimal Spanning Tree

## Representation

![Screen Shot 2020-09-02 at 7.49.37 PM.png](32BF4263082FEAAC74C8023360C114B3.png)

## Growing MST

Grows one edge a time. The generic method manages a set of edges A, maintaining the following loop invariant:

**Prior to each iteration, A is a subset of some MST**

At each step, we determine an edge (u, v) thatcan add to A without violating this invariant.

## Kruskal's Algorithm

Kruskal’s algorithm builds a minimum spanning tree by greedily adding edges to a graph that initially only contains the nodes of the original graph and no edges. The algorithm goes through the edges of the original graph **ordered by their weights** and always adds an edge to the new graph if the edge **does not create a cycle**.
The algorithm maintains the components of the new graph. Initially, each node of the graph belongs to a separate component. Always when an edge is added to the graph, two components are joined. Finally, all nodes belong to the same component, and a minimum spanning tree has been found. 