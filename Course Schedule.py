from collections import deque
def canFinish(numCourses, prerequisites):
    # Write your code here
    graph = {i: [] for i in range(numCourses)}

    indegree = [0] * numCourses
    for courseNum, prerequisite in prerequisites:
        graph[prerequisite].append(courseNum)
        indegree[courseNum] += 1

    queue, count = deque([]), 0
    order = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        order.append(node)
        count+=1
        for x in graph[node]:
            indegree[x] -=1
            if indegree[x] == 0:
                queue.append(x)
    return count == numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    print(canFinish(numCourses,prerequisites))