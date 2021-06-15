#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (45.10%)
# Likes:    3685
# Dislikes: 237
# Total Accepted:    583.8K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#

from Python.commons.BinaryTree import BinaryTree, TreeNode

# @lc code=start
from typing import Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.

        A height-balanced binary tree is defined as:
        A binary tree in which the left and right subtrees of
        every node differ in height by no more than 1.

        :param root: the root of a binary tree
        :return: True if the binary tree is height-balanced; False otherwise
        """
        if not root:
            return True
        return self.dfs_iterative_soln(root)

    def dfs_iterative_soln(self, root: TreeNode) -> bool:
        """
        DFS Recursive Single-Pass Solution

        Similar as Multi-Pass solution, but use -1 as return value
        to annotate that the subtree is not balanced

        Runtime: O(n)
        Space: O(log(n))
        """
        def recurse(node: TreeNode) -> int:
            if not node:
                return 0

            leftHeight = recurse(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = recurse(node.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1

        return recurse(root) != -1

    def dfs_multi_pass_soln(self, root: TreeNode) -> bool:
        """
        DFS Recursive Multi-Pass Solution

        Recursively calculate and check the height

        Base Case:
        - The current node is a leaf
            - height is 0 and return True trivially

        Recursive Case:
        - The current node is not a leaf
            - get the height and check balance for left and right subtree
            - the current height is 1 + max child height
            - the current node is balanced if both child nodes are balanced and
              the child nodes' heights are different by no more than 1

        Runtime: O(n * log(n))
        Space: O(log(n))
        """
        def recurse(node: TreeNode) -> Tuple[int, bool]:
            if node is None:
                return 0, True
            left_height, left_balance = recurse(node.left)
            right_height, right_balance = recurse(node.right)

            curr_height = 1 + max(left_height, right_height)
            curr_balance = left_balance and right_balance and \
                abs(left_height - right_height) <= 1
            return curr_height, curr_balance

        return recurse(root)[1]


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = BinaryTree([3, 9, 20, None, None, 15, 7]).get_root()
    expected = True
    actual = Solution().isBalanced(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = BinaryTree([1, 2, 2, 3, 3, None, None, 4, 4]).get_root()
    expected = False
    actual = Solution().isBalanced(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = BinaryTree([]).get_root()
    expected = True
    actual = Solution().isBalanced(input1)
    print("Test case 3")
    print(actual)
    print(expected)
