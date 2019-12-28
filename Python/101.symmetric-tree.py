#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (45.14%)
# Likes:    3010
# Dislikes: 71
# Total Accepted:    516.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
#

# @lc code=start


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.iterative_soln(root)

    def iterative_soln(self, root: TreeNode) -> bool:
        """
        Iteratively check

        Runtime: O(n)
        Space: O(log(n))
        """
        queue = []
        queue.insert(0, root)
        queue.insert(0, root)
        while len(queue) > 0:
            left = queue.pop(0)
            right = queue.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.insert(0, left.left)
            queue.insert(0, right.right)
            queue.insert(0, left.right)
            queue.insert(0, right.left)
        return True

    def recursive_soln(self, root: TreeNode) -> bool:
        """
        Recursively check

        Runtime: O(n)
        Space: O(log(n))
        """
        def helper(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and \
                helper(left.left, right.right) and \
                helper(left.right, right.left)

        return helper(root, root)
# @lc code=end


if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(3)
    print(Solution().isSymmetric(node), True)
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(2)
    node.right = TreeNode(2)
    node.right.left = TreeNode(2)
    print(Solution().isSymmetric(node), False)
