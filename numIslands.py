from collections import deque

def numIslands(grid):
        if len(grid) == 0:
                return 0
        num = 0
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j] == '1':
                                num += 1
                                bfs(grid, len(grid), len(grid[0]), [i, j])

        return num


def bfs(grid, rowLength, colLength, coordinate):
        queue = deque([coordinate])
        print(queue)
        while queue:
                currentPoint = queue.popleft()

                neighbors = getValidNeighbor(rowLength, colLength, currentPoint[0], currentPoint[1])

                for neighbor in neighbors:

                        if grid[neighbor[0]][neighbor[1]] == '1':
                                queue.append(neighbor)
                                grid[neighbor[0]][neighbor[1]] = "#"


def getValidNeighbor(rowLength, colLength, row, col):
        result = []
        if 0 <= row - 1 < rowLength and 0 <= col < colLength:
                # if grid[row - 1][col] == 1:
                result.append((row - 1, col))
        if 0 <= row < rowLength and 0 <= col - 1 < colLength:
                # if grid[row][col-1] == 1:
                result.append((row, col - 1))
        if 0 <= row + 1 < rowLength and 0 <= col < colLength:
                # if grid[row+1][col] == 1:
                result.append((row + 1, col))
        if 0 <= row < rowLength and 0 <= col + 1 < colLength:
                # if grid[row][col+1] == 1:
                result.append((row, col + 1))
        return result
if __name__ == '__main__':
        grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

        print(numIslands(grid))






