#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (28.93%)
# Likes:    4212
# Dislikes: 178
# Total Accepted:    405.1K
# Total Submissions: 1.4M
# Testcase Example:
# '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#
#
#

# @lc code=start
from typing import Dict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    capacity: int
    head: Node
    tail: Node
    cache: Dict[int, Node]

    def __init__(self, capacity: int):
        """
        Init dummy head and tail and connect them together
        """
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        """
        Get the value corresponding to the key.
        If the key is not stored, return -1.
        """
        if key in self.cache:
            curr = self.cache[key]
            self._remove_node(curr)
            self._add_node(curr)
            return curr.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Store or update a key value pair
        """
        if key in self.cache:
            self._remove_node(self.cache[key])
        curr = Node(key, value)
        self.cache[key] = curr
        self._add_node(curr)
        if len(self.cache) > self.capacity:
            # pop tail
            tail = self.tail.prev
            self._remove_node(tail)
            self.cache.pop(tail.key)
        return

    def _add_node(self, node: Node) -> None:
        """
        Add a node to the head
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return

    def _remove_node(self, node: Node) -> None:
        """
        Remove a node from the linked list
        """
        prev = node.prev
        temp = node.next

        prev.next = temp
        temp.prev = prev
        return
# @lc code=end


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1), -1)
    print(cache.get(2), 3)
    # print(cache.get(1), -1)
    # print(cache.get(3), 3)
    # print(cache.get(4), 4)
