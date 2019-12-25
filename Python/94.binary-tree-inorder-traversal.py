#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (59.85%)
# Likes:    2249
# Dislikes: 96
# Total Accepted:    586.6K
# Total Submissions: 979.6K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.morris_soln(root)

    def morris_soln(self, root: TreeNode) -> List[int]:
        """
        Morris Traversal
        (https://leetcode.com/problems/binary-tree-inorder-traversal/solution/)

        Utilizes Threaded Binary Tree by reforming the tree to form a
        single-child tree
        """
        res = []
        curr = root
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None:
                    prev = prev.right
                prev.right = curr
                tmp = curr
                curr = curr.left
                tmp.left = None
        return res

    def iterative_soln(self, root: TreeNode) -> List[int]:
        """
        Iteratively traverse the binary tree

        This traversal uses a stack because stack provides us
        a way to backtrack
        """
        res = []
        stack = []
        curr = root
        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def recursive_soln(self, root: TreeNode) -> List[int]:
        """
        Recursively inorder traverse the binary tree
        """
        res = []

        if root is None:
            return res
        res.extend(self.recursive_soln(root.left))
        res.append(root.val)
        res.extend(self.recursive_soln(root.right))

        return res

# @lc code=end


if __name__ == "__main__":
    node = TreeNode(1)
    node.right = TreeNode(2)
    node.right.left = TreeNode(3)
    print(Solution().inorderTraversal(node))
