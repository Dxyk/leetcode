#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (60.79%)
# Likes:    2385
# Dislikes: 39
# Total Accepted:    401.5K
# Total Submissions: 657.2K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# Output:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
#
#
from typing import List


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_node(lst: List[int]) -> TreeNode:
    """
    Create a Binary Tree using BFS according to the per-layer list
    """
    if len(lst) == 0:
        return None
    forest = [TreeNode(item) for item in lst]
    count = len(forest)
    for i, tree in enumerate(forest):
        left_index = 2 * i + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * i + 2
        if right_index < count:
            tree.right = forest[right_index]

    return forest[0]  # root


def get_list(node: TreeNode) -> List[int]:
    """
    Get the list of values by level under the node
    """
    res = []
    curr_level = [node]
    while curr_level:
        next_level = []
        for n in curr_level:
            if n:
                res.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
        curr_level = next_level
    return res
# @lc code=start


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.iterative_soln(root)

    def iterative_soln(self, root: TreeNode) -> TreeNode:
        """
        Iteratively invert the tree
        """
        queue = [root]
        while len(queue) != 0:
            next_queue = []
            for curr in queue:
                if curr is not None:
                    next_queue.insert(0, curr.right)
                    next_queue.insert(0, curr.left)
                    curr.left, curr.right = curr.right, curr.left
            queue = next_queue
        return root

    def recursive_soln(self, root: TreeNode) -> TreeNode:
        """
        Recursively invert the tree
        """
        def helper(node: TreeNode) -> TreeNode:
            if node is not None:
                left_temp, right_temp = node.left, node.right
                node.left = helper(right_temp)
                node.right = helper(left_temp)
            return node
        return helper(root)

# @lc code=end


if __name__ == "__main__":
    node = create_node([4, 2, 7, 1, 3, 6, 9])
    print(get_list(node))
    print(get_list(Solution().invertTree(node)))
    print([4, 7, 2, 9, 6, 3, 1])
