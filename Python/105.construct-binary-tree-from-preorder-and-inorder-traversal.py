#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (44.67%)
# Likes:    2371
# Dislikes: 63
# Total Accepted:    283.9K
# Total Submissions: 634.2K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.iterative_soln(preorder, inorder)

    def iterative_improved_soln(self, preorder: List[int],
                                inorder: List[int]) -> TreeNode:
        """
        Improves the Iterative solution

        Runtime: O(n^2) since recurse for each element and search in each call
        Space: O(log(n)) since size of stack == depth
        """
        if len(preorder) == len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)

        preorder_start = 1
        inorder_start = 0
        while preorder_start < len(preorder):
            curr = TreeNode(preorder[preorder_start])
            preorder_start += 1
            prev = None
            while len(stack) != 0 and stack[-1].val == inorder[inorder_start]:
                prev = stack.pop()
                inorder_start += 1
            if prev is not None:
                prev.right = curr
            else:
                stack[-1].left = curr
            stack.append(curr)
        return root

    def iterative_soln(self, preorder: List[int],
                       inorder: List[int]) -> TreeNode:
        """
        Iterative solution

        Idea:
        1. keep pushing the nodes from the preorder into a stack
           (and keep making the tree by adding nodes to the left of the
           previous node) until the top of the stack matches the first inorder.
        2. pop the top of the stack until the top does not equal inorder
           (keep a flag to note that you have made a pop).
        3. if the flag is set, insert a node to the right and reset the flag.
        4. Repeat 1 and 2 until preorder is empty.
        """
        if len(preorder) == len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)

        curr = root
        preorder_start = 1
        inorder_start = 0
        has_popped = False
        while preorder_start < len(preorder):
            if len(stack) == 0 or stack[-1].val != inorder[inorder_start]:
                if not has_popped:
                    curr.left = TreeNode(preorder[preorder_start])
                    curr = curr.left
                else:
                    has_popped = False
                    curr.right = TreeNode(preorder[preorder_start])
                    curr = curr.right
                stack.append(curr)
                preorder_start += 1
            else:
                curr = stack.pop()
                has_popped = True
                inorder_start += 1
        return root

    def recursive_soln(self, preorder: List[int],
                       inorder: List[int]) -> TreeNode:
        """
        Recursively build the tree

        Idea:
        - Preorder's first element provides the root value
        - Inorder's root value separates the left and right subtree.

        Runtime: O(n^2) since recurse for each element and search in each call
        Space: O(log(n)) since num recurse == depth
        """
        if len(preorder) == len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        inorder_root_idx = inorder.index(root.val)  # O(n)
        left_inorder = inorder[: inorder_root_idx]
        left_preorder = preorder[1: inorder_root_idx + 1]
        right_inorder = inorder[inorder_root_idx + 1:]
        right_preorder = preorder[inorder_root_idx + 1:]
        root.left = self.recursive_soln(left_preorder, left_inorder)
        root.right = self.recursive_soln(right_preorder, right_inorder)
        return root
# @lc code=end


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    built = Solution().buildTree(preorder, inorder)
    print(built.val)
    print(built.left.val, built.right.val)
    print(built.right.left.val, built.right.right.val)
