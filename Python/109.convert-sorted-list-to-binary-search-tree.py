#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (52.29%)
# Likes:    3317
# Dislikes: 102
# Total Accepted:    314.3K
# Total Submissions: 600.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [0]
# Output: [0]
#
#
# Example 4:
#
#
# Input: head = [1,3]
# Output: [3,1]
#
#
#
# Constraints:
#
#
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#

from Python.commons.BinaryTree import BinaryTree, TreeNode
from Python.commons.LinkedList import ListNode, LinkedList

# @lc code=start
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Given the head of a singly linked list where
        elements are sorted in ascending order,
        convert it to a height balanced BST.

        :param head: the head of a sorted singly linked list
        :return: a height balanced BST using the values from the linked list
        """
        return self.recursive_ll_soln(head)

    def recursive_ll_soln(self, head: ListNode) -> TreeNode:
        """
        Recursive Solution by traversing the LinkedList

        Find midpoint using a pair of slow/fast pointers

        Runtime: O(N)
        Space: O(N)
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # cut off the left half
        prev.next = None

        root = TreeNode(slow.val)
        root.left = self.recursive_ll_soln(head)
        root.right = self.recursive_ll_soln(slow.next)
        return root

    def recursive_list_soln(self, head: ListNode) -> TreeNode:
        """
        Recursive Solution by converting the linked list to a list

        Find the mid point and build the balanced BST
        See 108-convert-sorted-list-to-binary-search-tree

        Runtime: O(n)
        Space: O(n)
        """
        def convert_to_list(head: ListNode) -> List:
            res = []
            curr = head
            while curr:
                res.append(curr.val)
                curr = curr.next
            return res

        def recurse(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(array[mid])
            node.left = recurse(left, mid - 1)
            node.right = recurse(mid + 1, right)
            return node

        array = convert_to_list(head)
        return recurse(0, len(array) - 1)


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = LinkedList([-10, -3, 0, 5, 9]).get_head()
    expected = BinaryTree([0, -3, 9, -10, None, 5]).get_root()
    actual = Solution().sortedListToBST(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = LinkedList([]).get_head()
    expected = BinaryTree([]).get_root()
    actual = Solution().sortedListToBST(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = LinkedList([0]).get_head()
    expected = BinaryTree([0]).get_root()
    actual = Solution().sortedListToBST(input1)
    print("Test case 3")
    print(actual)
    print(expected)

    # Test Case 4
    input1 = LinkedList([1, 3]).get_head()
    expected = BinaryTree([3, 1]).get_root()
    actual = Solution().sortedListToBST(input1)
    print("Test case 4")
    print(actual)
    print(expected)
