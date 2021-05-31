#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (46.62%)
# Likes:    2558
# Dislikes: 147
# Total Accepted:    597.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#
#
#
from Python.commons.LinkedList import LinkedList, ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Given the head of a sorted linked list,
        delete all duplicates such that each element
        appears only once.
        Return the linked list sorted as well.

        :param head: The head of the sorted linked list
        :return: The head of the list with each element appearing once
        """
        if not head:
            return head
        return self.one_pointer(head)

    def one_pointer(self, head: ListNode) -> ListNode:
        """
        One Pointer Solution

        Improved base on the two pointer solution
        - Dummy is not necessary since the first duplicated node
        can be kept
        - Two pointers are not necessary, since we don't need
        to keep track of the previous node

        Runtime: O(n)
        Space: O(1)
        """
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head

    def two_pointer(self, head: ListNode) -> ListNode:
        """
        Two Pointer Solution

        - Use dummy head to avoid duplicated head node
        - Use pre pointer to keep track of the last safe node
        - Use curr pointer to check if the curr node and the next node are dup
        - If dup:
            - while dup, curr = curr.next
            - pre.next = curr
        - If not dup:
            - move pre and curr to next

        Runtime: O(n)
        Space: O(1)
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = LinkedList([1, 1, 2]).get_head()
    expected = LinkedList([1, 2]).get_head()
    actual = Solution().deleteDuplicates(input1)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = LinkedList([1, 1, 2, 3, 3]).get_head()
    expected = LinkedList([1, 2, 3]).get_head()
    actual = Solution().deleteDuplicates(input1)
    print("Test case 2")
    print(actual)
    print(expected)
