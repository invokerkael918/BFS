from collections import deque


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        if len(s) == 0 or len(dict) == 0:
            return -1
        queue = deque([s])
        visited = set([s])
        result = len(s)
        while queue:
            string = queue.popleft()
            result = min(result, len(string))
            for key in dict:
                index = string.find(key)
                while index != -1:
                    new_string = string[:index] + string[index + len(key):]
                    index = string.find(key, index + len(key))
                    if new_string not in visited:
                        queue.append(new_string)
                        visited.add(new_string)
        return result
