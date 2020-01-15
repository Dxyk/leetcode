#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (41.40%)
# Likes:    2760
# Dislikes: 156
# Total Accepted:    373.1K
# Total Submissions: 893.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
#
#
# Note:
#
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
        return self.iterative_improved_soln(root, p, q)

    def iterative_improved_soln(self, root: TreeNode,
                                p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Iterative solution

        Keep a pointer that points to the potential solution

        Runtime: O(n)
        Space: O(1)
        """
        neither_found = 2
        both_found = 0

        stack = [(root, neither_found)]

        found_one = False

        res_idx = -1

        # post order traversal
        while stack:
            parent_node, parent_num_found = stack[-1]

            if parent_num_found != both_found:

                if parent_num_found == neither_found:
                    if parent_node == p or parent_node == q:
                        if found_one:
                            return stack[res_idx][0]
                        else:
                            found_one = True
                            res_idx = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right

                # Update node state
                stack.pop()
                stack.append((parent_node, parent_num_found - 1))

                if child_node:
                    stack.append((child_node, neither_found))
            else:
                if found_one and res_idx == len(stack) - 1:
                    res_idx -= 1
                stack.pop()

        return None

    def iterative_soln(self, root: TreeNode,
                       p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Iterative solution

        Use a hashmap to keep track of the parent nodes

        Runtime: O(n)
        Space: O(n)
        """
        stack = [root]
        parent_dict = {root: None}

        # Traverse and build parent dict until we've seen both p and q
        while p not in parent_dict or q not in parent_dict:
            node = stack.pop()
            if node.left:
                parent_dict[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_dict[node.right] = node
                stack.append(node.right)

        # A set of nodes in the path from root to p
        p_path = set()

        curr = p
        while curr:
            p_path.add(curr)
            curr = parent_dict[curr]

        curr = q
        while curr not in p_path:
            curr = parent_dict[curr]
        return curr

    def recursive_soln(self, root: TreeNode,
                       p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Recursive solution

        The lowest common ancestor is the node that for the first time
        contains both trees in two of [left, right, curr] subtrees.

        Runtime: O(n)
        Space: O(n)
        """
        res = [None]

        def helper(node: TreeNode) -> bool:
            if not node:
                return False
            left_res = helper(node.left)
            right_res = helper(node.right)

            curr_res = node == p or node == q

            if curr_res + left_res + right_res >= 2:
                res[0] = node
            return curr_res or left_res or right_res
        helper(root)
        return res[0]

# @lc code=end


if __name__ == "__main__":
    node = create_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    sub1 = node.left
    sub2 = node.right
    res = Solution().lowestCommonAncestor(node, sub1, sub2)
    print(get_list(res))
    print(get_list(node))

    node = create_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    sub1 = node.left
    sub2 = node.left.right.right
    res = Solution().lowestCommonAncestor(node, sub1, sub2)
    print(get_list(res))
    print(get_list(node))
