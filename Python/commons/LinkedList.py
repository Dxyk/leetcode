from __future__ import annotations

from typing import List, Optional, TypeVar

T = TypeVar('T')


# LinkedList and ListNode Definitions
class ListNode:
    """
    A ListNode object in a Linked List.

    This class is supported by LeetCode.

    Attributes:
    :param val: The value contained in the current node
    :param next: The next node that is connected to the current node
    """

    val: T
    next: Optional[ListNode]

    def __init__(self, x: T, next_node: Optional[ListNode] = None):
        """
        Initialize a List Node.

        Runtime: O(1)
        Space: O(1)

        :param x: The value contained in the node
        :param next: The next list node connected to the current node
                     NOTE: The next param is not supported by LeetCode
        """
        self.val = x
        self.next = next_node

    def __str__(self) -> str:
        """
        Returns the string format of the current List Node.
        The whole list following the current node will be stringified
        as well.

        The format will be
        `node1.val->node2.val->node3.val`

        Runtime: O(n)
        Space: O(n)

        :return: The string representation of the ListNode
        """
        vals: List[str] = []
        curr: ListNode = self

        while curr is not None:
            vals.append(str(curr.val))
            curr = curr.next

        return "->".join(vals)


class LinkedList:
    """
    A LinkedList containing multiple ListNodes.

    This class is used for testing, and is NOT supported by LeetCode.

    TODO: Add common algorithms

    Attributes:
    :param head: The head of the LinkedList
    """

    _head: ListNode

    def __init__(self, items: List[T]):
        """
        Initialize a LinkedList base on a list

        Runtime: O(n)
        Space: O(n)

        :param items: The list of items in the LinkedList
        """
        dummy = ListNode(None)
        curr = dummy
        for n in items:
            curr.next = ListNode(n)
            curr = curr.next

        self._head = dummy.next

    def get_head(self) -> ListNode:
        """
        Get the head ListNode

        :return: The head ListNode
        """
        return self._head
