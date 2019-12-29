#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (45.44%)
# Likes:    2011
# Dislikes: 260
# Total Accepted:    286.1K
# Total Submissions: 628.4K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
# ⁠    1
# ⁠   / \
# ⁠  2   5
# ⁠ / \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
# ⁠ \
# ⁠  2
# ⁠   \
# ⁠    3
# ⁠     \
# ⁠      4
# ⁠       \
# ⁠        5
# ⁠         \
# ⁠          6
#
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.recursive_soln(root)

    def iterative_soln(self, root: TreeNode) -> None:
        """
        Iterative solution

        Runtime: O(n) since preorder traversal
        Space: O(n) since stack size n
        """
        if root is not None:
            stack = []
            stack.append(root)
            while len(stack) != 0:
                curr = stack.pop()
                if curr.right is not None:
                    stack.append(curr.right)
                if curr.left is not None:
                    stack.append(curr.left)
                if len(stack) != 0:
                    curr.right = stack[-1]
                curr.left = None
        return

    def recursive_soln(self, root: TreeNode) -> None:
        """
        Recursive solution

        Recursively move the left subtree to the right

        Runtime: O(n^2) since flattening the whole list and search for right
            most node for each call
        Space: O(n) since flatten every node
        """
        def helper(node: TreeNode, last: TreeNode) -> TreeNode:
            if node is None:
                return last
            node.right = helper(node.left, helper(node.right, last))
            node.left = None
            return node
        # if root is not None:
        #     left = right = None
        #     if root.left is not None:
        #         self.recursive_soln(root.left)
        #         left = root.left
        #     if root.right is not None:
        #         self.recursive_soln(root.right)
        #         right = root.right
        #     if left is not None:
        #         root.right = root.left
        #         root.left = None
        #         curr = root.right
        #         # this could be optimized so that we don't have to search for
        #         # the right most node every time
        #         while curr.right:
        #             curr = curr.right
        #         curr.right = right
        return helper(root, None)
# @lc code=end


if __name__ == "__main__":
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right = TreeNode(5)
    node.right.right = TreeNode(6)
    Solution().flatten(node)
    while node is not None:
        print(node.val)
        node = node.right
