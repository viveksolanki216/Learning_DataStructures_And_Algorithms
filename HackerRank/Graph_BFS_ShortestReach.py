# Problem Link: https://www.hackerrank.com/challenges/bfsshortreach/problem?isFullScreen=true
# Date: 09 Jul 2025
# Code By: Vivek Singh Solanki

# !/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    print(n, m, edges, s)

    # First initialize the graph
    graph = {i: [] for i in range(1, n + 1)}
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(graph)

    # Initialize the distance array, this will also act as if the node is visited or not
    distance = [-1] * (n + 1)

    # Set the distance of start node to itself = 0 and add to the queue
    distance[s] = 0
    queue = deque([s])
    while queue:
        print("queue: ", queue)
        current = queue.popleft()
        print("current: ", current)
        # add all un-visited neighbor nodes of current to queue
        # also keep adding the distance for each un-visited neighbor
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                print("neighbor", neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[current] + 6
                print(distance)
    print(distance)

    return distance[1:s] + distance[s + 1:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

