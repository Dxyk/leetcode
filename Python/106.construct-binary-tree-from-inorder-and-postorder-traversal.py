#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (50.89%)
# Likes:    2787
# Dislikes: 53
# Total Accepted:    303.5K
# Total Submissions: 596.4K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
#
#
#
from typing import List
from Python.commons.BinaryTree import TreeNode, BinaryTree

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Given two integer arrays inorder and postorder where
        - Inorder is the inorder traversal of a binary tree
        - Postorder is the postorder traversal of the same tree
        - All values are unique
        Construct and return the binary tree

        :param inorder: The inorder traversal of the binary tree
        :param postorder: The postorder traversal of the binary tree
        :return: The constructed tree base on inorder and postorder
        """
        return self.recursive_dict_soln(inorder, postorder)

    def recursive_dict_soln(self, inorder: List[int],
                            postorder: List[int]) -> TreeNode:
        """
        Recursive Solution using Dictionary
        Use a dict (hashmap) to store the value to inorder index mapping
        Keep track of the start and end indices to avoid destroying lists

        Runtime: O(n)
        Space: O(n)
        """
        val_to_idx = dict()
        for idx, val in enumerate(inorder):
            val_to_idx[val] = idx

        def recurse(inorder_start: int, inorder_end: int, postorder_start: int,
                    postorder_end: int) -> TreeNode:
            if inorder_start > inorder_end:
                return None
            root = TreeNode(postorder[postorder_end])
            inorder_idx = val_to_idx[root.val]
            dist = inorder_idx - inorder_start
            root.left = recurse(inorder_start, inorder_idx - 1,
                                postorder_start, postorder_start + dist - 1)
            root.right = recurse(inorder_start + dist + 1, inorder_end,
                                 postorder_start + dist, postorder_end - 1)
            return root

        return recurse(0, len(inorder) - 1, 0, len(postorder) - 1)

    def recursive_soln(self, inorder: List[int],
                       postorder: List[int]) -> TreeNode:
        """
        Recursive solution

        Base case:
        The inorder list or the postorder list is empty -> return None

        Recursive case:
        1. Use the postorder's last element as the current node
        2. Find the index of the node value in the inorder list
            i. Everything on the left is in the left tree
            ii. Everything on the right is in the right tree
        3. Build the right tree recursively
        4. Build the left tree recursively

        NOTE:
        - The right then left order is important due to the nature of postorder
            - The second last element is the node on the right
        - The postorder list will be destroyed with this implementation

        Runtime: O(n^2)
        Space: O(n^2)
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorder_idx = inorder.index(root.val)

        root.right = self.recursive_soln(inorder[inorder_idx + 1:], postorder)
        root.left = self.recursive_soln(inorder[:inorder_idx], postorder)

        return root


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = [9, 3, 15, 20, 7]
    input2 = [9, 15, 7, 20, 3]
    expected = BinaryTree([3, 9, 20, None, None, 15, 7]).get_root()
    actual = Solution().buildTree(input1, input2)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 1
    input1 = [-1]
    input2 = [-1]
    expected = BinaryTree([-1]).get_root()
    actual = Solution().buildTree(input1, input2)
    print("Test case 2")
    print(actual)
    print(expected)
