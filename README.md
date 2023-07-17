Graph representations
-----------------

Implement a topological sorting method that works in 2 distinct stages:
- Calculating "put on stack" and "take off stack" labels for each vertex.
- Checking acyclicity by counting return arcs.
  
A procedure that calculates the labels should be implemented for one selected graph representation. The procedure of counting return arcs should be implemented in 3 versions,
using:
- an adjacency matrix
- a list of successors
- an arcs list.
  
Generate random directed graphs for at least 10 different values ​​of n with densities d = 0.2 and 0.4.

Task 1. Measure the duration of the label calculation step depending on the number n.

Task 2. Count return arcs depending on the number n and the density for every graph representation.

Task 3. For every graph representation calculate the duration of the return arc counting step depending on the number n and the density.


Repository contains code required to solve given tasks.
