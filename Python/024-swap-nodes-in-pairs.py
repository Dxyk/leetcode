from __future__ import annotations

from typing import List


# LinkedList and ListNode Definitions
class ListNode:
    val: int
    next: ListNode

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


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        """
        Given a linked list, swap every two adjacent nodes and return its head.

        You may not modify the values in the list's nodes, only nodes itself may be changed.

        >>> print(Solution().swap_pairs(LinkedList([1, 2, 3, 4]).get_start()))
        2->1->4->3

        :param head: The head of the linked list
        :return: The swapped list node's head
        """
        return self.my_soln(head)

    def my_soln(self, head: ListNode) -> ListNode:
        """
        T: O()
        Disconnect the link in the middle and swap

        A->B->C
        B->C, A
        B->A->C

        :param head: The head of the linked list
        :return: The swapped list node's head
        """
        if not head or not head.next:
            return head
        second = head.next
        prev = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            prev.next = nxt
            head = head.next
            prev = nxt.next
        return second

    def brute_force(self, head: ListNode) -> ListNode:
        """
        T: O(n)
        The brute force solution.

        :param head: The head of the linked list
        :return: The swapped list node's head
        """
        lst = []
        ptr = head
        # O(n) get all values in a list
        while ptr:
            lst.append(ptr.val)
            ptr = ptr.next

        # O(n) swap each two pairs
        for i in range(1, len(lst), 2):
            lst[i - 1], lst[i] = lst[i], lst[i - 1]

        # O(n) regenerate the linked list
        dummy_head = ptr = ListNode(-1)
        for i in lst:
            ptr.next = ListNode(i)
            ptr = ptr.next

        return dummy_head.next
