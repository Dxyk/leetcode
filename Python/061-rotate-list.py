from Python.commons.LinkedList import LinkedList, ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Given a linked list, rotate the list to the right by k places, where k is non-negative.

        >>> ll = LinkedList([1, 2, 3, 4, 5])
        >>> print(Solution().rotateRight(ll.get_start(), 2))
        4->5->1->2->3
        >>> ll = LinkedList([0, 1, 2])
        >>> print(Solution().rotateRight(ll.get_start(), 4))
        2->0->1

        :param head: the head node
        :param k: the number of places to rotate right by
        :return: the new head of the list node
        """
        if not head or not head.val or k < 0:
            return head
        return self.brute_force(head, k)

    def brute_force(self, head: ListNode, k: int) -> ListNode:
        """
        The brute force solution

        :param head: the head node
        :param k: the number of places to rotate right by
        :return: the new head of the list node
        """
        curr = head
        while k > 0:
            if not curr.next:
                curr = head
            else:
                curr = curr.next
            k -= 1
        return head
