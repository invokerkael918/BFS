from collections import deque
def findOrder(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses
    for courseNum, prerequisite in prerequisites:
        graph[prerequisite].append(courseNum)
        indegree[courseNum] += 1

    queue, order = deque([]), []

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        order.append(node)
        for x in graph[node]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)
    if len(order) == numCourses:
        return order
    return []

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(numCourses,prerequisites))