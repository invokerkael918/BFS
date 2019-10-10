"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if root is None:
            return []
        # write your code here
        result = []
        # 起点放入root
        queue = deque([root])

        while queue:
            # 用来存储当前层的node value
            level = []
            # for 当前层，找到下一层
            for _ in range(len(queue)):
                # 拿出最左边的
                node = queue.popleft()
                level.append(node.val)
                # 两个if 找到下一层
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result



