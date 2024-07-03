#!/usr/bin/python3
""" lockboxes algorithm for the lockbox interview """

from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return True

    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]

        for key in keys:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
