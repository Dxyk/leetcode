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
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        """
        Given a linked list, remove the n-th node from the end of list and return its head.

        >>> ll = LinkedList([1, 2, 3, 4, 5])
        >>> result = Solution().remove_nth_from_end(ll.get_start(), 2)
        >>> print(result)
        1->2->3->5

        >>> ll = LinkedList([4,5,4])
        >>> result = Solution().remove_nth_from_end(ll.get_start(), 1)
        >>> print(result)
        4->5

        :param head: the head of the list node
        :param n: the nth element to remove from the end
        :return: the head of the resulting list node
        """
        return self.one_pass_soln(head, n)

    def one_pass_soln(self, head: ListNode, n: int) -> ListNode:
        """
        O(n)
        use two pointers instead of one.
        first pointer sets the distance from the second so that we can know when the second pointer has reached the desired position
        second is the actual pointer that makes the changes

        :param head: the head of the list node
        :param n: the nth element to remove from the end
        :return: the head of the resulting list node
        """
        dummy_head = ListNode(-1)
        dummy_head.next = first_ptr = second_ptr = head
        # move first forward for n + 1 steps to be ahead of the second ptr
        for i in range(n + 1):
            first_ptr = first_ptr.next
        # when the first reaches the end, the second reaches the nth from the end.
        while first_ptr is not None:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        second_ptr.next = second_ptr.next.next
        return dummy_head.next

    def brute_force(self, head: ListNode, n: int) -> ListNode:
        """
        O(2n) = O(n)

        :param head: the head of the list node
        :param n: the nth element to remove from the end
        :return: the head of the resulting list node
        """
        dummy_head = ListNode(-1)
        dummy_head.next = ptr = head
        length = 0

        # first pass: count the length
        while ptr is not None:
            length += 1
            ptr = ptr.next

        length -= n
        ptr = dummy_head

        # second pass: reconstruct ll until the nth from the end. skip n and connect the rest
        while length > 0:
            length -= 1
            ptr = ptr.next
        ptr.next = ptr.next.next

        return dummy_head.next


def main():
    Solution()


if __name__ == '__main__':
    main()
