# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.



# BFS: use a set() to mark visited
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited: # 这个位点没有被visited过并且为1，从它做BFS找到它的完整连通块
                    self.bfs(grid, i, j, visited) # 当这个bfs函数执行完毕即找完了一个以i，j开始的连通块（岛），该连通块中每个等于1的小块都是visited过了的
                    islands += 1

        return islands

    
    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = collections.deque([(x, y)])
        visited.add((x, y))

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):  # 判断next_x，next_y坐标位点的值是不是在当前的BFS搜索中的有效位点：没越界没visited过且等于1，则有效
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    
    def is_valid(self, grid, x, y, visited):
        n, m  = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):   # 越界
            return False
        if (x, y) in visited:                 # visited过
            return False
        return grid[x][y] == "1"              # 没有越界，没有visited过，值为1，is_valid为true




# BFS: use a boolean grid to mark visited
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0 

        m, n = len(grid), len(grid[0])
        count = 0
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, i, j, visited)
                    count += 1

        return count
    
    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
        queue = collections.deque([(x, y)])
        visited[x][y] = True  ## 入队要mark
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1' and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
        
    


        





















    






        

            






        



       