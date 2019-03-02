from typing import List


# LinkedList and ListNode Definitions
class ListNode:
    val: int
    next: 'ListNode'  # python 3.6- uses 'ClassName' where as python 3.7+ uses 'from __future__ import annotations'

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return it as a new list.
        The new list should be made by splicing together the nodes of the first two lists.

        >>> print(Solution().mergeTwoLists(LinkedList([1, 2, 4]).get_start(), LinkedList([1, 3, 4]).get_start()))
        1->1->2->3->4->4

        :param l1: list node 1
        :param l2: list node 2
        :return: the resulting merged list node's head
        """
        return self.my_soln(l1, l2)

    def recursion_soln(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T: O(n)

        :param l1: list node 1
        :param l2: list node 2
        :return: the resulting merged list node's head
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.recursion_soln(l1.next, l2)
        return l1 or l2

    def iterative_better_soln(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T: O(n)

        :param l1: list node 1
        :param l2: list node 2
        :return: the resulting merged list node's head
        """
        if None in (l1, l2):
            return l1 or l2
        result_head_dummy = ptr = ListNode(-1)
        result_head_dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = ptr.next
                ptr.next = l2
                temp = l2.next
                l2.next = nxt
                l2 = temp
            ptr = ptr.next
        # don't need to continue the loop. can just point the head to the list with remaining elements
        ptr.next = l1 or l2
        return result_head_dummy.next

    def my_soln(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T: O(n)

        :param l1: list node 1
        :param l2: list node 2
        :return: the resulting merged list node's head
        """
        ptr1, ptr2 = l1, l2
        result_head_dummy = ptr = ListNode(-1)
        while ptr1 or ptr2:
            if not ptr1:
                ptr.next = ListNode(ptr2.val)
                ptr = ptr.next
                ptr2 = ptr2.next
            elif not ptr2:
                ptr.next = ListNode(ptr1.val)
                ptr = ptr.next
                ptr1 = ptr1.next
            else:
                if ptr1.val <= ptr2.val:
                    ptr.next = ListNode(ptr1.val)
                    ptr1 = ptr1.next
                else:
                    ptr.next = ListNode(ptr2.val)
                    ptr2 = ptr2.next
                ptr = ptr.next
        return result_head_dummy.next


def main():
    print(Solution().mergeTwoLists(LinkedList([1, 2, 4]).get_start(), LinkedList([1, 3, 4]).get_start()))


if __name__ == '__main__':
    main()
