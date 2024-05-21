# Description
# Given an undirected graph in which each edge's length is 1, and two nodes from the graph. Return the length of the shortest path between two given nodes.

# About the representation of graph

# Example
# Example 1:

# Input: graph = {1,2,4#2,1,4#3,5#4,1,2#5,3}, node1 = 3, node2 = 5
# Output: 1
# Explanation:
#   1------2  3
#    \     |  | 
#     \    |  |
#      \   |  |
#       \  |  |
#         4   5
# Example 2:

# Input: graph = {1,2,3,4#2,1,3#3,1#4,1,5#5,4}, node1 = 1, node2 = 5
# Output: 2



"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, A, B):
        # Write your code here
        queue = collections.deque([A])
        distance = {A: 0}
        while queue:
            curr = queue.popleft()
            if curr == B:
                return distance[B]
            
            for neighbor in curr.neighbors:
                if neighbor not in distance:
                    distance[neighbor] = distance[curr] + 1
                    queue.append(neighbor)
                
        return -1