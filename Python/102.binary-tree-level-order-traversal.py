#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (51.29%)
# Likes:    2065
# Dislikes: 56
# Total Accepted:    482.8K
# Total Submissions: 939.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.iterative_soln(root)

    def iterative_soln(self, root: TreeNode) -> List[List[int]]:
        """
        Iteratively traverse the tree with the depth of the current level

        Runtime: O(n)
        Space: O(log(n))
        """
        res = []
        if root is not None:
            queue = []
            queue.insert(0, root)
            while len(queue) > 0:
                level_num = len(queue)
                curr_level_res = []
                for _ in range(level_num):
                    curr = queue.pop()
                    if curr.left is not None:
                        queue.insert(0, curr.left)
                    if curr.right is not None:
                        queue.insert(0, curr.right)
                    curr_level_res.append(curr.val)
                res.append(curr_level_res)
        return res

    def recursive_soln(self, root: TreeNode) -> List[List[int]]:
        """
        Recursively traverse the tree with the depth of the current level

        Runtime: O(n)
        Space: O(log(n))
        """
        res = []

        def helper(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            while len(res) < depth + 1:
                res.append([])
            res[depth].append(node.val)
            if node.left is not None:
                helper(node.left, depth + 1)
            if node.right is not None:
                helper(node.right, depth + 1)

        helper(root, 0)
        return res


# @lc code=end
if __name__ == "__main__":
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(Solution().levelOrder(node))
    soln = [
        [3],
        [9, 20],
        [15, 7]
    ]
    print(soln)
