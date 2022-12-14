# CSC4120 Project

<br/>

# Input format
You will read in a `.txt` file to construct the tree, which is in adjacency list format.

The first line contains one integer $ N $, where $ N $ is the number of nodes in the tree.

In each line of the following $ N $ lines, the first integer represents a node, followed by all its neighbors, separated by space.

For example,
``` python
11
1 2 3 4
2 5 6
3
4 7 8 9
5 10
6 11
7
8
9
10
11
```
corresponds to the example in your description file.

# Generator
We provide a `generator.py` file to generator random trees.

To make the virus spread longer, we construct the trees in such a way that each node has a degree in range [0, MAX_DEGREE], with higher probability for larger degrees. The tree is limited in depth by MAX_DEPTH.

## Run
``` python
python generator.py $MAX_DEGREE $MAX_DEPTH $out
```
where out is the path for the output file. If not all parameters are given, the program will use default values: MAX_DEGREE = 4, MAX_DEPTH = 15, out = 'test.txt'.

# Two-player game
For the two-play game, you may need to assign colors to the nodes. You can randomly assign color to each node as long as the total numbers of two kinds of nodes are the same (except the root, no one can save it).