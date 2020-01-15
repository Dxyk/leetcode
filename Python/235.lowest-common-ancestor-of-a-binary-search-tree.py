#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (47.32%)
# Likes:    1531
# Dislikes: 93
# Total Accepted:    346.2K
# Total Submissions: 727.9K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
#
# Note:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
#
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
    while len(curr_level) != 0:
        next_level = []
        for curr in curr_level:
            if curr is not None:
                res.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
        curr_level = next_level
    return res


# @lc code=start

class Solution:
    def lowestCommonAncestor(self, root: TreeNode,
                             p: TreeNode, q: TreeNode) -> TreeNode:
        return self.iterative_soln(root, p, q)

    def iterative_soln(self, root: TreeNode,
                       p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Iterative solution

        This is kinda a hack since we are gauranteed that both p and q will be
        in the tree

        Runtime: O(n)
        Space: O(1)
        """
        if not root:
            return None
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

    def recursive_soln(self, root: TreeNode,
                       p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Recursive solution

        Runtime: O(n)
        Space: O(n)
        """
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.recursive_soln(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.recursive_soln(root.right, p, q)
        else:
            return root

# @lc code=end


if __name__ == "__main__":
    node = create_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    sub1 = node.left
    sub2 = node.right
    res = Solution().lowestCommonAncestor(node, sub1, sub2)
    print(get_list(res))
    print(get_list(node))

    node = create_node([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    sub1 = node.left
    sub2 = node.left.right
    res = Solution().lowestCommonAncestor(node, sub1, sub2)
    print(get_list(res))
    print(get_list(sub1))
