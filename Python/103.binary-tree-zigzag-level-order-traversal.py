#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (50.31%)
# Likes:    3544
# Dislikes: 130
# Total Accepted:    520.5K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#

from Python.commons.BinaryTree import BinaryTree, TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Given the root of a binary tree, return the
        zigzag level order traversal of its nodes' values.
        I.e., from left to right, then right to left for
        the next level and alternate between.

        :param root: The root of a binary tree
        :return: The zigzag level order traversal of nodes under root
        """
        if not root:
            return []
        return self.bfs_soln(root)

    def bfs_soln(self, root: TreeNode) -> List[List[int]]:
        """
        BFS Solution

        Use a queue to perform BFS.

        - Odd levels (also root) - right to left, reverse curr level
        - Even levels - left to right, curr level

        Runtime: O(n)
        Space: O(log(n))
        """
        res = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                curr_node = queue.pop(0)
                if curr_node:
                    level.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            if level:
                if len(res) % 2 == 0:
                    res.append(level)
                else:
                    res.append(level[::-1])
        return res


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = BinaryTree([3, 9, 20, None, None, 15, 7]).get_root()
    expected = [[3], [20, 9], [15, 7]]
    actual = Solution().zigzagLevelOrder(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = BinaryTree([1]).get_root()
    expected = [[1]]
    actual = Solution().zigzagLevelOrder(input1)
    print("Test case 2")
    print(actual)
    print(expected)

    # Test Case 3
    input1 = BinaryTree([]).get_root()
    expected = []
    actual = Solution().zigzagLevelOrder(input1)
    print("Test case 3")
    print(actual)
    print(expected)

    # Test Case 4
    input1 = BinaryTree([1, 2, 3, 4, None, None, 5]).get_root()
    expected = [[1], [3, 2], [4, 5]]
    actual = Solution().zigzagLevelOrder(input1)
    print("Test case 4")
    print(actual)
    print(expected)
