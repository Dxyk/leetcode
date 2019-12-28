#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (26.78%)
# Likes:    2793
# Dislikes: 408
# Total Accepted:    537.3K
# Total Submissions: 2M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#

# @lc code=start
from typing import Tuple


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.iterative_traversal_soln(root)

    def iterative_traversal_soln(self, root: TreeNode) -> bool:
        """
        Iterative traversal solution
        """
        if root is None:
            return True
        stack = []
        curr = root
        prev = None
        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None and curr.val <= prev.val:
                return False
            prev = curr
            curr = curr.right
        return True

    def recursive_traversal_soln(self, root: TreeNode) -> bool:
        """
        Recursive traversal solution
        """
        def helper(node: TreeNode) -> Tuple[bool, int, int]:
            max_val = -float("inf")
            min_val = float("inf")
            if node is None:
                return True, max_val, min_val
            if node.left:
                left_valid, max_left, min_left = helper(node.left)
                if not left_valid or max_left >= node.val:
                    return False, max_val, min_val
                max_val = max(max_left, max_val)
                min_val = min(min_left, min_val)
            if node.right:
                right_valid, max_right, min_right = helper(node.right)
                if not right_valid or min_right <= node.val:
                    return False, max_val, min_val
                max_val = max(max_right, max_val)
                min_val = min(min_right, min_val)
            max_val = max(node.val, max_val)
            min_val = min(node.val, min_val)
            return True, max_val, min_val
        return helper(root)[0]
# @lc code=end


if __name__ == "__main__":
    node1 = TreeNode(2)
    node1.left = TreeNode(1)
    node1.right = TreeNode(3)
    print(Solution().isValidBST(node1), True)

    node2 = TreeNode(5)
    node2.left = TreeNode(1)
    node2.left.left = TreeNode(3)
    node2.left.right = TreeNode(6)
    node2.right = TreeNode(4)
    print(Solution().isValidBST(node2), False)
