#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (54.19%)
# Likes:    3336
# Dislikes: 88
# Total Accepted:    732.1K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
#
#
#

from Python.commons.BinaryTree import TreeNode, BinaryTree

# @lc code=start
from typing import List, Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Given the roots of two binary trees p and q,
        Return True if the two binary trees are the same,
        False otherwise.

        :param p: The first binary tree
        :param q: The second binary tree
        :return: True if the two binary trees are the same; False otherwise
        """
        return self.bfs_recursive_soln(p, q)

    def bfs_recursive_soln(self, p: TreeNode, q: TreeNode) -> bool:
        """
        BFS Recursive Solution (Level order traversal)

        Runtime: O(n)
        Space: O(log(n))
        """
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.bfs_recursive_soln(p.left, q.left) and \
                    self.bfs_recursive_soln(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False

    def bfs_iterative_soln(self, p: TreeNode, q: TreeNode) -> bool:
        """
        BFS Iterative Solution (Level order traversal)

        Runtime: O(n)
        Space: O(log(n))
        """
        queue: List[Tuple[TreeNode, TreeNode]] = [(p, q)]

        while queue:
            curr_p, curr_q = queue.pop()
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                else:
                    queue.insert(0, (curr_p.left, curr_q.left))
                    queue.insert(0, (curr_p.right, curr_q.right))
            elif not curr_p and not curr_q:
                continue
            else:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = BinaryTree([1, 2, 3]).get_root()
    input2 = BinaryTree([1, 2, 3]).get_root()
    expected = True
    actual = Solution().isSameTree(input1, input2)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = BinaryTree([1, 2]).get_root()
    input2 = BinaryTree([1, None, 2]).get_root()
    expected = False
    actual = Solution().isSameTree(input1, input2)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = BinaryTree([1, 2, 1]).get_root()
    input2 = BinaryTree([1, 1, 2]).get_root()
    expected = False
    actual = Solution().isSameTree(input1, input2)
    print("Test case 3")
    print(actual)
    print(expected)
