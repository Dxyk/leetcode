#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (55.98%)
# Likes:    2243
# Dislikes: 250
# Total Accepted:    427.5K
# Total Submissions: 763.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the bottom-up level order traversal
# of its nodes' values. (i.e., from left to right, level by level from leaf to
# root).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        Given the root of a binary tree, return the bottom-up
        level order traversal of its nodes' values.
        (i.e., from left to right, level by level from leaf to root).

        :param root: the root of a binary tree
        :return: The bottom-up level order traversal of the nodes
        """
        if not root:
            return []
        return self.bfs_soln(root)

    def bfs_soln(self, root: TreeNode) -> List[List[int]]:
        """
        BFS Solution

        Use BFS to level order traverse the list, and revert the
        level order traversal to obtain the bottom-up traversal

        Runtime: O(n)
        Space: O(n)
        """
        traversal = []
        queue = [root]
        while queue:
            curr_level = []
            curr_count = len(queue)
            while curr_count > 0:
                curr_node = queue.pop(0)
                curr_level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                curr_count -= 1
            traversal.append(curr_level)
        return traversal[::-1]


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = BinaryTree([3, 9, 20, None, None, 15, 7]).get_root()
    expected = [[15, 7], [9, 20], [3]]
    actual = Solution().levelOrderBottom(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = BinaryTree([1]).get_root()
    expected = [[1]]
    actual = Solution().levelOrderBottom(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = BinaryTree([]).get_root()
    expected = []
    actual = Solution().levelOrderBottom(input1)
    print("Test case 3")
    print(actual)
    print(expected)
