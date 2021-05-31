from __future__ import annotations

from typing import List, Optional, TypeVar

T = TypeVar('T')


# BinaryTree and TreeNode Definitions
class TreeNode:
    """
    A TreeNode object in a BinaryTree.

    This class is supported by LeetCode.

    Attributes:
    :param val: The value contained in the current node
    :param left: The left node that is connected to the current node
    :param right: The right node that is connected to the current node
    """

    val: T
    left: Optional[TreeNode]
    right: Optional[TreeNode]

    def __init__(self,
                 x: T,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        """
        Initializes a TreeNode with its value, left node and right node.

        Runtime: O(1)
        Space: O(1)

        :param x: The value contained in the TreeNode
        :param left: The left node, defaults to None
        :param right: The right node, defaults to None
        """
        self.val = x
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Returns the string representation of the current TreeNode.
        The whole subtree under the current TreeNode will be stringified
        as well.

        The stringified TreeNode will be the BFS traversal of the tree.

        Runtime: O(n)
        Space: O(log(n))

        :return: The string representation of the current TreeNode
        """
        traversed: List[str] = []
        queue: List[TreeNode] = [self]
        height = 0
        while queue:
            count = len(queue)
            curr_level = []
            while count > 0:
                curr = queue.pop(0)
                if curr:
                    curr_level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    curr_level.append(None)
                count -= 1
            curr_level.extend([None] * (2**height - len(curr_level)))
            traversed.append(str(curr_level))
            height += 1

        return "[\n" + "\t\n".join(traversed) + "\n]"


class BinaryTree:
    """
    A BinaryTree containing multiple TreeNodes.

    This class is used for testing, and is NOT supported by LeetCode.

    Attributes:
    :param root: The root of the BinaryTree
    """

    _root: Optional[TreeNode]

    def __init__(self, items: List[T]) -> None:
        """
        Initializes a BinaryTree using a list of items.
        The list of items is a per-layer list.
        I.e. The list obtained by performing BFS on the BinaryTree

        Runtime: O(n)
        Space: O(n)

        :param items: The per-layer list of items
        """
        if len(items) == 0:
            self._root = None
        else:
            nodes = [
                TreeNode(item) if item is not None else None for item in items
            ]
            count = len(nodes)

            for i, node in enumerate(nodes):
                left_idx = 2 * i + 1
                if left_idx < count:
                    node.left = nodes[left_idx]

                right_idx = 2 * i + 2
                if right_idx < count:
                    node.right = nodes[right_idx]

            self._root = nodes[0]

    def get_root(self) -> TreeNode:
        """
        Gets the root of the BinaryTree

        Runtime: O(1)
        Space: O(1)

        :return: The root of the BinaryTree
        """
        return self._root
