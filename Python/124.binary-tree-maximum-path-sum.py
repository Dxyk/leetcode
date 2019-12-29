#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (31.80%)
# Likes:    2361
# Dislikes: 186
# Total Accepted:    256K
# Total Submissions: 803.5K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
#   -10
#   / \
#  9  20
#    /  \
#   15   7
#
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        return self.recursive_global_max_soln(root)

    def recursive_global_max_soln(self, root: TreeNode) -> int:
        """
        Recursive solution by updating a global maximum variable
        """
        self.res = -float("inf")

        def helper(node: TreeNode) -> int:
            if node is None:
                return 0
            left_res = helper(node.left)
            right_res = helper(node.right)
            self.res = max(self.res, left_res + right_res + node.val)
            return max(node.val + max(left_res, right_res), 0)
        helper(root)
        return self.res

    def recursive_soln(self, root: TreeNode) -> int:
        """
        Recursive solution by returning two values every call.

        The helper returns two values:
        - the max value when root is in the path (can only be a linked list)
        - the max value when the path starts with the root (can be a tree)
        """
        def helper(node: TreeNode) -> Tuple[int, int]:
            if node is None:
                return -float("inf"), -float("inf")
            left_root, left_sub = helper(node.left)
            right_root, right_sub = helper(node.right)
            all_subs = [left_root, left_sub, right_root, right_sub,
                        node.val + left_root + right_root]
            return node.val + max(left_root, right_root, 0), max(all_subs)
        return max(helper(root))
# @lc code=end


if __name__ == "__main__":
    node = TreeNode(-10)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(Solution().maxPathSum(node), 42)
    node = TreeNode(-2)
    node.right = TreeNode(-1)
    print(Solution().maxPathSum(node), -1)
    node = TreeNode(1)
    node.left = TreeNode(-2)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(3)
    node.left.left.left = TreeNode(-1)
    node.right = TreeNode(-3)
    node.right.left = TreeNode(-2)
    print(Solution().maxPathSum(node), 3)
