# Do not use Prufer sequence
# Each node has degree in [0, MAX_DEGREE]
# with higher probability for larger degress
# Intend to let the virus spread longer
# The tree is limited by a maximum depth MAX_DEPTH

import sys
import random

if __name__ == "__main__":
    try:
        MAX_DEGREE = int(sys.argv[1])
        MAX_DEPTH = int(sys.argv[2])
        out = sys.argv[3]
    except:
        MAX_DEGREE = 4
        MAX_DEPTH = 15
        out = 'test.txt'

    degrees = [i for i in range(MAX_DEGREE)]
    degrees.extend(degrees[2:])
    degrees.extend(degrees[3:])
    nodes = [[1, 2, 3]]
    level = [1, 2, 3]
    depth = 1
    total = 4
    while depth < MAX_DEPTH:
        nextLevel = []
        while level:
            node = level.pop(0)
            degree = random.choice(degrees)
            children = [total + i for i in range(degree)]
            total += degree
            nodes.append(children)
            nextLevel.extend(children)
        level = nextLevel
        depth += 1

    with open(out, 'w') as f:
        f.write("%d\n"%total)
        for node in range(total):
            try:
                f.write(str(node + 1) + ' ' + ' '.join([str(i + 1) for i in nodes[node]]) + '\n')
            except:
                f.write(str(node + 1) + '\n')

    print("Generated a tree with", total, "nodes")
