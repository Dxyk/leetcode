#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (31.10%)
# Likes:    2273
# Dislikes: 555
# Total Accepted:    323.3K
# Total Submissions: 1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#
# Constraints:
#
#
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
#
#
#

# @lc code=start


class Node:
    # Definition for a Node.
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.in_place_modification_soln(head)

    def in_place_modification_soln(self, head: 'Node') -> 'Node':
        """
        Modify the original head and then separate the lists
        https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491

        1. Iterate the original list and duplicate each node. The duplicate
           of each node follows its original immediately.
        2. Iterate the new list and assign the random pointer for each
           duplicated node.
        3. Restore the original list and extract the duplicated nodes.

        Runtime: O(n)
        Space: O(1)
        """
        # Assume head: 1 -> 2 -> 3 -> 4
        # with 1.random = 3, 2.random = 4
        curr = head
        # Results in: 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        # with 1.random = 3, 2.random = 4
        while curr is not None:
            temp = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = temp
            curr = temp

        curr = head
        # Results in: 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        # with 1.random = 3, 1'.random = 3', 2.random = 4, 2'.random = 4'
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy_head = Node(-1)
        copy_curr = copy_head
        # Results in: 1 -> 2 -> 3 -> 4, 1' -> 2' -> 3' -> 4'
        # with 1.random = 3, 1'.random = 3', 2.random = 4, 2'.random = 4'
        while curr is not None:
            temp = curr.next.next
            # extract copy list
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            # resume original list
            curr.next = temp
            curr = curr.next

        return copy_head.next

    def hashmap_soln(self, head: 'Node') -> 'Node':
        """
        Hashmap solution

        Use Two passes:
        - first store the nodes in the hashmap with idx:node as kvp
        - then map each node's rand to the random node in the original ll

        Runtime: O(n)
        Space: O(n)
        """
        curr = head
        rand_dict = {}
        while curr:
            rand_dict[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            # use dict.get() to set default as None
            rand_dict[curr].next = rand_dict.get(curr.next)
            rand_dict[curr].random = rand_dict.get(curr.random)
            curr = curr.next
        return rand_dict.get(head)
# @lc code=end
