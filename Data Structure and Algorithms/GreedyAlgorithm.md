# Greedy Algorithm

**Overview:**
  - It is an algorithmic paradigm that builds up a solution piece by piece.
  - It always chooses the next piece that offers _the most obvious_ and _immediate_ benefit. 
  - Greedy fits perfectly for those solutions in which choosing a locally optimal solution leads to global optimal solution (a.k.a **Greedy Choice**)

Examples: 
  - Insertion sort
  - Selection sort
  - Topological sort
  - Prim's MST
  - Kruskal MST
  - Activity Selection problem
  - Coin Change problem
  - Fractional Knapsack problem


**Activity Selection problem:**
  - We are given 'n' activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single acitivity at at time
  - Solution: Sort activities based on their finish time and pick the first activities and then continue by greedily picking the next activity that its start time is greater than or equal of the finish time of the previous one. 
  - Time complexity O(n*log n)
  - Space complexity O(log n)  --> because of sorting

**Coin Change problem:**
  - Given a value V, we want to make changes for that V dollar. We have infinite supply of each of the denominations {1,5,10, 20, 50, 100} notes. which is the minimum number of notes needed to make the changes for $V. 
  - Solution: initialize results as empty. find the largest denomination that is small than V. add found denomination to the result. Subtract value of found denomination from V, and continue until V become 0. 
  - Time complexity O(n) --> search
  - Space complexity O(V)  --> number of items in the result array
**Fractional Knapsack problem:**
  - Fill the knapsack such that the value is maximum and total weight is utmost W. items can be broken down to maximize the knapsack value. 
  - Solution: First calculate the ratio(Value/Weight) for each item. Then sort the items based on this ratio. Take the items with the highest ration sequentially until weight allows. At the end, add the next item as much (fractional) as we can. 
  - Time complexity O(n*log n) --> sort
  - Space complexity O(n)  --> sort










