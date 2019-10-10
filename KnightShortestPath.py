from collections import deque

def shortestPath(grid, source, destination):
    queue = deque([source])
    des = (destination[0],destination[1])
    Step = 0
    while queue:

        currentPoint = queue.popleft()
        next_steps = getValidSteps(grid, len(grid), len(grid[0]), currentPoint[0], currentPoint[1])
        if des not in next_steps:
            Step+=1
            grid[currentPoint[0]][currentPoint[1]] = "#"
        else:
            return Step

        for next_step in next_steps:
            queue.append(next_step)
    return 0

def getValidSteps(grid,rowLength,colLength,row,col):
    result = []
    if 0 <=row+1 < rowLength and 0 <= col+2 < colLength:
        if grid[row + 1][col+2] == 0:
            result.append((row+1, col+2))

    if 0 <=row+1 < rowLength and 0 <= col-2 < colLength:
        if grid[row + 1][col - 2] == 0:
            result.append((row+1, col-2))

    if 0 <=row-1 < rowLength and 0 <= col+2 < colLength:
        if grid[row - 1][col + 2] == 0:
            result.append((row-1, col+2))

    if 0 <=row-1 < rowLength and 0 <= col-2 < colLength:
        if grid[row - 1][col - 2] == 0:
            result.append((row-1, col-2))

    if 0 <=row+2 < rowLength and 0 <= col+1 < colLength:
        if grid[row + 2][col + 1] == 0:
            result.append((row+2, col+1))

    if 0 <=row+2 < rowLength and 0 <= col-1 < colLength:
        if grid[row + 2][col - 1] == 0:
            result.append((row+2, col-1))

    if 0 <=row-2 < rowLength and 0 <= col+1 < colLength:
        if grid[row - 2][col + 1] == 0:
            result.append((row-2, col+1))

    if 0 <=row-2 < rowLength and 0 <= col-1 < colLength:
        if grid[row - 2][col - 1] == 0:
            result.append((row-2, col-1))

    return result


    # (row + 1, col + 2)
    # (row + 1, col - 2)
    # (row - 1, col + 2)
    # (row - 1, col - 2)
    # (row + 2, col + 1)
    # (row + 2, col - 1)
    # (row - 2, col + 1)
    # (row - 2, col - 1)
if __name__ == '__main__':
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    source = [2,0]
    destination = [2,2]
    print(shortestPath(grid,source,destination))