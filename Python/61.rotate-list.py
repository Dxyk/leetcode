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
        >>> ll = LinkedList([1])
        >>> print(Solution().rotateRight(ll.get_start(), 1))
        1

        :param head: the head node
        :param k: the number of places to rotate right by
        :return: the new head of the list node
        """
        if not head or head.val is None or k <= 0:
            return head
        return self.two_pointer(head, k)

    def two_pointer(self, head: ListNode, k: int) -> ListNode:
        """
        The two pointer solution
        1. loop through the ll to get the count
        2. k %= count
        3. head -> ... -> left -> ...k nodes... -> right -> None
        4. return left.next -> ... -> right -> head -> ... -> left -> None

        :param head: the head node
        :param k: the number of places to rotate left by
        :return: the new head of the list node
        """
        # count total
        curr = ListNode(-1)
        curr.next = head
        count = 0

        while curr.next:
            curr = curr.next
            count += 1

        # mod k so that we only have to loop once
        k %= count
        if not k:
            return head

        # use two pointers to keep track of the last k nodes
        # left will have the last k nodes in the end
        # right will be k nodes away from left and will be at the last node in the end
        left = right = head

        while k > 0:
            right = right.next
            k -= 1

        while right.next:
            left = left.next
            right = right.next
        # head -> ... -> left -> left.next -> ... -> right -> None

        temp = left.next
        # head -> ... -> left -> left.next -> ... -> right -> None
        # temp (left.next) -> ... -> right -> None

        left.next = None
        # head -> ... -> left -> None
        # temp (left.next) -> ... -> right -> None

        right.next = head
        # temp (left.next) -> ... -> head -> ... -> left -> None

        head = temp
        # head (temp) (left.next) -> ... -> old_head -> ... -> left -> None

        return head


if __name__ == '__main__':
    ll = LinkedList([0, 1, 2])
    print(Solution().rotateRight(ll.get_head(), 4))
