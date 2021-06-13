#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (61.69%)
# Likes:    4067
# Dislikes: 288
# Total Accepted:    546.9K
# Total Submissions: 885.8K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
#
#
#

from typing import List
from Python.commons.BinaryTree import BinaryTree, TreeNode


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        Given an integer array nums where the elements are
        sorted in ascending order, convert it to a height-balanced
        binary search tree.

        A height-balanced binary tree is a binary tree in which
        the depth of the two subtrees of every node never differs
        by more than one.

        :param nums: a sorted ascending array of integers
        :return: a height-balanced BST from nums
        """
        if not nums:
            return None
        return self.recursive_index_soln(nums)

    def recursive_index_soln(self, nums: List[int]) -> TreeNode:
        """
        Recursive Solution using Index

        Similar solution as bellow, but avoids using slicing (expensive)
        and uses indices instead

        Runtime: O(n)
        Space: O(log(n))
        """
        def recurse(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = recurse(left, mid - 1)
            node.right = recurse(mid + 1, right)
            return node

        return recurse(0, len(nums) - 1)

    def recursive_soln(self, nums: List[int]) -> TreeNode:
        """
        Recursive Solution

        Recursively build the tree and its subtrees

        Base Case:
        - nums is empty, return None
        - nums has only 1 element, return a TreeNode of this element

        Recursive Case:
        - Find the mid point of nums
            - idx = (len + 1) // 2
        - Use mid point as node value
        - Build left subtree using left of the mid point
        - Build right subtree using right of the mid point

        Runtime: O(n*log(n)) # slicing is O(n)
        Space: O(log(n)) # height
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.recursive_soln(nums[:mid])
        node.right = self.recursive_soln(nums[mid + 1:])
        return node


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = [-10, -3, 0, 5, 9]
    expected = BinaryTree([0, -3, 9, -10, None, 5]).get_root()
    actual = Solution().sortedArrayToBST(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = [1, 3]
    expected = BinaryTree([3, 1]).get_root()
    actual = Solution().sortedArrayToBST(input1)
    print("Test case 2")
    print(actual)
    print(expected)
