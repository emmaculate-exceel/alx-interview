#!/usr/bin/env python3
""" lockboxes algorithm for the lockbox interview """

from collections import deque

def canUnlockAll(boxes):
    """ function that can unlock all boxes """
    n = len(boxes)
    if n == 0:
        return False
    
    visited = [False] * n
    visited[0] = True  # Start with the first box unlocked
    
    queue = deque([0])  # Start BFS from the first box
    
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)
    
    # Check if all boxes are visited
    return all(visited)

# Example usage:
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
