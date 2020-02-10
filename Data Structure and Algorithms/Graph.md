# Graphs

**Definition:**
  - Graph is a pair of sets (V,E), where V is the set of **Vertices** and E is the set of **Edges**, connecting the pair of vertices. 

**Terminologies:**
  - Vertices: nodes of the graph
  - Edges: arcs that connect pairs of vertices
  - Unweighted Graph: no weight is associated with any Edges
  - Weighted Graph: There is a weight associated with each Edge
  - Undirected Graph: no direction associated with any Edge
  - Directed Graph: There is a direction associated with each Edge
  - Cyclic Graph: a graph having at least one loop
  - Acyclic Graph: a graph having no loop
  - Tree: a special case of Directed Acyclic Graph (DAG)

**Types of Graphs (6 types):**
 - Directed
   * Weighted
     - Positive
     - Negative
   * Un-weighted
 - Undirected
   * Weighted
     - Positive
     - Negative
   * Un-weighted

**Graph representation in the memory:**
 - Adjacency matrix
 - Adjacency list

If a graph is 'complete' or 'near to complete', then we should use **adjacency matrix** ( otherwise there would be a lot of useless zeros). On the other hand, if the number of Edges are few, then we should use **adjacency list**. 

**Graph Traversal**
 - Breadth First Search (BFS)
    * Algorithm: It starts at some arbitrary node and explores the neighbor nodes at the same level first before moving to the next level. 
    * Implementation: It uses Queues. 
    * Time Complexity: O(V+E)
    * Space Complexity: O(V+E)
    * When to use: If we know that target vertex is close to starting point
 - Depth First Search (DFS)
    * Algorithm: It starts selecting some arbitrary node and explores as far as possible along each node before backtracking.
    * Implementation: It uses Stacks. 
    * Time Complexity: O(V+E)
    * Space Complexity: O(V+E)
    * When to use: If we know that target vertex is buried very deep

## Topological Sort

Algorithm: It sorts given action in such a way that if there is a dependancy of one action to another, then the dependent action always come later than its parent action. 

It uses Stack for implementation

Algorithm Time and Space complexity: O(V+E) 

## Sigle Source Shortest Path (SSSP)

SSSP : It is about finding a path b/w a given vertex (source) to all other vertices in a graph such that the total distance b/w them (source & destination) is minimum. 

Algorithms: 
  - BFS
  - Dijkstra
  - Bellman Ford

**BFS**
  - Can only work for _unweighted graphs_ . For weighted graphs, it doesn't work because BFS explores a given graph only in 'breadth way', but there can always be a better route which is not 'breadth-way'
  - Time and Space Complexity O(E)

Note: DFS can not be used for SSSP problem because it has the tendency to go 'as far as possible' from source, hence it can never find the shortest path. 

**Dijkstra Algorithm**

Algorithm: 
 - It sets the distance of all vertices to infinite and source vertex to zero
 - Then it saves all the vertices in _minHeap_
 - Then it iterates and extract minHeap and for each neighbor of the minHeap, if the minHeap's distance + currentEdge < neighbor's distance, then updates neighbor's distance and parent
  - Time Complexity: O(V^2)
  - Space Complexity: O(V)

Corner Case:
 - Negative Cycle (A graph w/ negative cycle doesn't have SSSP solution, so, there should be a mechanism to inform the user. However, Dijkstra doesn't have that mechanism. So, it is useless in case of negative cycles. 


**Bellman-Ford Algorithm**

The Bellman-Ford Algo. is used to find SSSP

If a graph contains a 'negative cycle', i.e. a cycle whose edges sum to a negative value, that is reachable form the source, then there is no shortest path. Any path that has a point on the negative cycle can be made shorter by one more walk around the negative cycle. In such a case, the Bellman-Ford algo. can **detect** 'negative cycle' and _report their existence_. 

Algorithm: 
  - It must be iterated **V-1** times
  - For each edge, we must check **if**(current 'distance' of destination vertex > 'distance' of source vertex + current weight b/w source and destination vertex) **then** update the distance of destination vertex w/ distance of source vertex + current weight b/w source and destination vertex. 
  - Time Complexity: O(VE)
  - Space Complexity: O(V)


**Comparing BFS, Dijkstra, and Bellman-Ford**
				BFS			Dijkstra			Bellman-Ford\ 
Time Complexity			O(V^2)			O(V^2)				O(V*E)\
Space Complexity		O(E)			O(V)				O(V)\
Implementation 			Easy			Moderate			Moderate\
Limitation			Weighted		Negative Cycle			N/A\
unWeighted Graph		**Preferred**		moderate implementation		moderate impelementation\
Weighted Graph			Not supported		**Preferred**			Don't use\
Negative Cycle			Not supported 		Not supported			**Preferred**\

## All Pair Shortest Path (APSP)
APSP: Finding a path between every vortex to all other vertices in a graph such that the total distance between them is minimum. 

BFS, Dijkstra, and Bellman-Ford works here. There time and space complexity will be multiplied by O(V) as we iterate the algorithm for all vertices. 

Another algorithm is Floyd-Warshal algorithm, which has a simpler implementation than Dijkstra, but it has the same issue with negative cycle. Time and space complexity of Floyd-Warshal is O(V^3) and O(V^2). 


## Minimum Spanning Tree (MST)

Solution:
  - Kruskal's algorithm
  - Prim's algorithm

**Kruskal's Algorithm:**

It is a greedy algorithm. It starts by adding increasing cost edges at each step and checks at each step that the cycle formation is avoided. The time and space complexities are as below:
  - Time Complexity: O(E*logE)
  - Space Complexity: O(V+E)

**Prim's Algorithm:**

It is a greedy algorithm. It starts by randomly taking a vertex as a source and mark its weight to zero and mark all other vertices to infinity. Then for every adjacent unvisited vertex of current vertex, **if** current weight of this 'adjacent vertex' is more than current edge, then update 'adjacent vertex's weight' to current edge weight. Do that step for all the vertices in increasing order or weights. The time and space complexities are as below:
  - Time Complexity: O(E*logV)
  - Space Complexity: O(V)

**Kruskal vs. Prim's**
  - Kruskal:
    * Algorithm's focus is on Edges
    * It finalizes one edge at every iteration
  - Prim's
    * Algorithm's focus is on Vertices
    * It finalizes one vertex at every iteration


