#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.39%)
# Likes:    2958
# Dislikes: 127
# Total Accepted:    333K
# Total Submissions: 837K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
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

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Given the head of a sorted linked list, delete all nodes that
        have duplicate numbers, leaving only distinct numbers
        from the original list. The returned list is sorted as well

        :param head: The head of a sorted linked list
        :return: The head of the sorted linked list without duplicated nodes
        """
        if not head:
            return head
        return self.two_pointer(head)

    def two_pointer(self, head: ListNode) -> ListNode:
        """
        Two Pointer Solution

        - Use dummy head to avoid duplicated head node
        - Use pre pointer to keep track of the last safe node
        - Use curr pointer to check if the curr node and the next node are dup
        - If dup:
            - while dup, curr = curr.next
            - exit while, curr = curr.next (don't want dup node at all)
            - pre.next = curr
        - If not dup:
            - move pre and curr to next

        Runtime: O(n)
        Space: O(1)
        """
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    from Python.commons.LinkedList import LinkedList

    # Test Case 1
    input1 = LinkedList([1, 2, 3, 3, 4, 4, 5])
    expected = [1, 2, 5]
    actual = Solution().deleteDuplicates(input1.get_head())
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = LinkedList([1, 1, 1, 2, 3])
    expected = [2, 3]
    actual = Solution().deleteDuplicates(input1.get_head())
    print("Test case 2")
    print(actual)
    print(expected)
