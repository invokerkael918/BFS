from collections import deque


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if len(grid) == 0:
            return 0
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and grid[row][col] != "#":
                    self.bfs(row, col, grid)
                    result += 1

        return result

    def bfs(self, x, y, grid):
        queue = deque([(x,y)])
        grid[x][y] = "#"
        while queue:
            x,y = queue.popleft()
            #neighbors = []
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = delta_x + x
                next_y = delta_y + y
                if not self.is_valid(next_x,next_y,grid):
                    continue
                queue.append((next_x,next_y))
                grid[next_x][next_y] = "#"


    # def isValidPoints(self, x,y, grid):
    #     return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if grid[x][y] == "#":
            return False
        return grid[x][y]

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]
    S = Solution().numIslands(grid)
    print(S)
