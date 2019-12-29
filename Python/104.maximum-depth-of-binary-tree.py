#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (63.23%)
# Likes:    1795
# Dislikes: 62
# Total Accepted:    652K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
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
    def maxDepth(self, root: TreeNode) -> int:
        return self.iterative_soln(root)

    def iterative_soln(self, root: TreeNode) -> int:
        """
        Iterative (BFS) solution

        Runtime: O(n) since looping through entire tree
        Space: O(log(n)) since need to maintain queue size of at most num leaf
        """
        max = 0
        if root is not None:
            curr = root
            queue = []
            queue.insert(0, curr)
            while len(queue) > 0:
                for _ in range(len(queue)):
                    curr = queue.pop()
                    if curr.left is not None:
                        queue.insert(0, curr.left)
                    if curr.right is not None:
                        queue.insert(0, curr.right)
                max += 1
        return max

    def recursive_soln(self, root: TreeNode) -> int:
        """
        Recursive solution

        Runtime: O(n) since looping through entire tree
        Space: O(log(n)) since n recursive calls
        """
        def helper(node: TreeNode) -> int:
            if node is None:
                return 0
            else:
                return 1 + max(helper(node.left), helper(node.right))

        return helper(root)
# @lc code=end


if __name__ == "__main__":
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(Solution().maxDepth(node), 3)
