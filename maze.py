directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def hasPath(self, maze, start, destination):
        # write your code here
        n = len(maze)
        m = len(maze[0])
        queue = deque([start])

        while queue:
            i, j = queue.popleft()
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in directions:
                next_x, next_y = i + x, j + y

                while 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] != 1:
                    next_x += x
                    next_y += y
                next_x -= x
                next_y -= y

                if maze[next_x][next_y] == 0:
                    queue.append([next_x, next_y])
        return False