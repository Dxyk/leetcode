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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Given a linked list, reverse the nodes of a linked list k at a time and
        return its modified list.

        k is a positive integer and is less than or equal to the length of the linked list.
        If the number of nodes is not a multiple of k then left-out nodes in the end should
        remain as it is.

        >>> print(Solution().reverseKGroup(LinkedList([1, 2, 3, 4, 5]).get_start(), 2))
        2->1->4->3->5
        >>> print(Solution().reverseKGroup(LinkedList([1, 2, 3, 4, 5]).get_start(), 3))
        3->2->1->4->5

        Note:
        - Only constant extra memory is allowed.
        - You may not alter the values in the list's nodes, only nodes itself may be changed.

        :param head: The head of the linked list
        :param k: The group size to revert
        :return: The reverted ListNode
        """
        return self.recursive_soln(head, k)

    def recursive_soln(self, head: ListNode, k: int) -> ListNode:
        """
        T: O()
        The recursive force solution

        :param head: The head of the linked list
        :param k: The group size to revert
        :return: The reverted ListNode
        """
        total, ptr = 0, head
        while ptr:
            total += 1
            ptr = ptr.next
        if k <= 1 or total < k:
            return head
        ptr, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = ptr
            ptr = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return ptr

    def iterative_soln(self, head: ListNode, k: int) -> ListNode:
        """
        T: O()
        The iterative force solution

        :param head: The head of the linked list
        :param k: The group size to revert
        :return: The reverted ListNode
        """
        # TODO
        if not head or not head.next or k <= 1:
            return head
        ptr, total = head, 0
        while ptr:
            total += 1
            ptr = ptr.next
        if k > total:
            return head
        dummy = prev = ListNode(0)
        dummy.next = head
        # totally total//k groups
        for i in range(total // k):
            # reverse each group
            node = None
            for j in range(k - 1):
                nxt = head.next
                head.next = node
                node = head
                head = nxt
            # update nodes and connect nodes
            tmp = head.next
            head.next = node
            prev.next.next = tmp
            tmp1 = prev.next
            prev.next = head
            head = tmp
            prev = tmp1
        return dummy.next

    def brute_force(self, head: ListNode, k: int) -> ListNode:
        """
        T: O(n)
        The brute force solution

        :param head: The head of the linked list
        :param k: The group size to revert
        :return: The reverted ListNode
        """
        lst = []
        ptr = head
        while ptr:  # O(n)
            lst.append(ptr.val)
            ptr = ptr.next

        for i in range(0, len(lst) - len(lst) % k, k):  # O (n/k)
            lst[i:i + k] = lst[i:i + k][::-1]  # O(k)

        dummy_head = ptr = ListNode(-1)
        for val in lst:  # O(n)
            ptr.next = ListNode(val)
            ptr = ptr.next
        return dummy_head.next
