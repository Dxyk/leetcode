from __future__ import annotations

from typing import List, Union


# LinkedList and ListNode Definitions
class ListNode:
    val: int
    next: Union[ListNode, None]

    def __init__(self, x: int):
        """
        init a linked list node

        :param x: the value contained in the node
        """
        self.val = x
        self.next = None

    def __str__(self):
        """
        Returns the string format of the whole list following the current node

        :return: the string representation of the ListNode
        """
        vals: List[str] = []
        ptr = self
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.next
        return "->".join(vals)


class LinkedList:
    head: ListNode

    def __init__(self, numbers: List[int]):
        """
        init a linked list with numbers

        :param numbers: the list of numbers the LinkedList represents
        """
        self.head = ListNode(0)
        ptr = self.head
        for n in numbers:
            ptr.next = ListNode(n)
            ptr = ptr.next
        self.head = self.head.next

    def get_start(self) -> ListNode:
        """
        Get the starting ListNode

        :return: the starting ListNode
        """
        return self.head
