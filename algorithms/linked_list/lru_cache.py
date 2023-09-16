"""link to the problem: https://leetcode.com/problems/lru-cache/"""
from collections import OrderedDict


class Solution:

    class V1DoubleLinkedListHashmap:
        """
        Time complexity: O(1) 700ms beats 70.81%
        Space complexity: O(n) 78.2mb beats 54.10%
        """
        class Node:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.prev = self.next = None

        class LRUCache:

            def __init__(self, capacity: int):
                self.capacity = capacity
                self.cache = {}
                # left - LRU and right - most recent (dummy nodes)
                self.left, self.right = Node(0, 0), Node(0, 0)
                self.left.next, self.right.prev = self.right, self.left

            # remove node from left
            def remove(self, node: Node):
                prev, nxt = node.prev, node.next
                prev.next, nxt.prev = nxt, prev

            # insert node at right
            def insert(self, node: Node):
                prev, nxt = self.right.prev, self.right
                prev.next = nxt.prev = node
                node.next, node.prev = nxt, prev

            def get(self, key: int) -> int:
                if key in self.cache:
                    self.remove(self.cache[key])
                    self.insert(self.cache[key])
                    return self.cache[key].val
                return -1

            def put(self, key: int, value: int) -> None:
                if key in self.cache:
                    self.remove(self.cache[key])
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])

                if len(self.cache) > self.capacity:
                    # remove from the list and delete the LRU from cache
                    lru = self.left.next
                    self.remove(lru)
                    del self.cache[lru.key]

    class V2OrderedDict:
        class LRUCache:
            """
            Time complexity: O(1) 576ms beats 98.7%
            Space complexity: O(n) 77.4mb beats 83.15%
            """
            def __init__(self, capacity: int):
                self.capacity = capacity
                self.cache = OrderedDict()

            def get(self, key):
                if key in self.cache:
                    # Move the accessed key to the end (most recently used)
                    self.cache.move_to_end(key)
                    return self.cache[key]
                else:
                    return -1  # Key not found

            def put(self, key, value):
                if key in self.cache:
                    # Update the value and move the key to the end (most recently used)
                    self.cache[key] = value
                    self.cache.move_to_end(key)
                else:
                    # Check if the cache is full and evict the least recently used item
                    if len(self.cache) >= self.capacity:
                        self.cache.popitem(last=False)  # Remove the first (least recently used) item
                    # Add the new key-value pair to the end (most recently used)
                    self.cache[key] = value
