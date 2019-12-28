#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (37.80%)
# Likes:    1650
# Dislikes: 134
# Total Accepted:    163K
# Total Submissions: 430.7K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.dp_soln(n)

    def dp_soln(self, n: int) -> List[TreeNode]:
        """
        DP Solution
        """
        if n == 0:
            return []

        def helper(i: int, n: int) -> None:
            res = []
            if i > n:
                res.append(None)
                return res
            if i == n:
                res.append(TreeNode(i))
                return res
            for j in range(i, n + 1):
                left_trees = helper(i, j - 1)
                right_trees = helper(j + 1, n)

                for left_node in left_trees:
                    for right_node in right_trees:
                        curr_node = TreeNode(j)
                        curr_node.left = left_node
                        curr_node.right = right_node
                        res.append(curr_node)
            return res

        return helper(1, n)
# @lc code=end


if __name__ == "__main__":
    soln = [
        [1, None, 3, 2],
        [3, 2, None, 1],
        [3, 1, None, None, 2],
        [2, 1, 3],
        [1, None, 2, None, 3]
    ]

    print(Solution().generateTrees(3))
    print(soln)
