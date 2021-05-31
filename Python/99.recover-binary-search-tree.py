#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (42.63%)
# Likes:    2519
# Dislikes: 93
# Total Accepted:    213.5K
# Total Submissions: 494.6K
# Testcase Example:  '[1,3,null,null,2]'
#
# You are given the root of a binary search tree (BST), where exactly two nodes
# of the tree were swapped by mistake. Recover the tree without changing its
# structure.
#
# Follow up: A solution using O(n) space is pretty straight forward. Could you
# devise a constant space solution?
#
#
# Example 1:
#
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3
# makes the BST valid.
#
#
# Example 2:
#
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2
# and 3 makes the BST valid.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

from Python.commons.BinaryTree import TreeNode, create_node, get_list


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Given root of a BST, where exactly 2 nodes of the
        tree were swapped by mistake. Recover the tree in place
        without changing its structure

        :param root: The root of the BST
        """
        if root:
            self.stack_in_order_soln(root)

    def morris_traversal_soln(self, root):
        """
        Morris Traversal Solution

        TODO: understand this

        Runtime: O(n)
        Space: O(1)
        """
        curr, prev = root, TreeNode(float('-inf'))
        drops = []
        while curr:
            if curr.left:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right = curr
                    curr = curr.left
                    continue
                temp.right = None
            if curr.val < prev.val:
                drops.append((prev, curr))
            prev = curr
            curr = curr.right
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

    def stack_in_order_soln(self, root: TreeNode) -> None:
        """
        Stack In Order Solution

        Use a stack to iteratively traverse the tree

        Runtime: O(n)
        Space: O(log(n))
        """
        curr, prev = root, TreeNode(float('-inf'))
        drops, stack = [], []
        while curr or stack:
            # left
            while curr:
                stack.append(curr)
                curr = curr.left
            # mid
            node = stack.pop()

            # register if invalid
            if node.val < prev.val:
                drops.append((prev, node))
            prev = node

            # right
            curr = node.right

        # swap smallest larger with largest smaller
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

    def recursive_soln(self, root: TreeNode) -> None:
        """
        Recursive solution

        Use Recursive In Order Traversal to build the in order list.
        Swap the item that is larger than the next with the last item that
        is smaller than the next

        e.g. [1, 4, 3, 2, 5] -> [1, 2, 3, 4, 5]

        Runtime: O(n)
        Space: O(n + log(n))
        """
        res = []

        def recurse(node: TreeNode):
            if node:
                recurse(node.left)
                res.append(node)
                recurse(node.right)

        recurse(root)

        larger, smaller = None, None
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val and not larger:
                larger = res[i]
            if res[i].val > res[i + 1].val and larger:
                smaller = res[i + 1]
        larger.val, smaller.val = smaller.val, larger.val


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = create_node([1, 3, None, None, 2])
    expected = create_node([3, 1, None, None, 2])
    Solution().recoverTree(input1)
    print("Test case 1")
    print(get_list(input1))
    print(get_list(expected))

    # Test Case 2
    input1 = create_node([3, 1, 4, None, None, 2])
    expected = create_node([2, 1, 4, None, None, 3])
    Solution().recoverTree(input1)
    print("Test case 2")
    print(get_list(input1))
    print(get_list(expected))
