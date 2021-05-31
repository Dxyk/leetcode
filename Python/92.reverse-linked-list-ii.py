#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (40.73%)
# Likes:    3713
# Dislikes: 194
# Total Accepted:    354.3K
# Total Submissions: 863K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#

from Python.commons.LinkedList import LinkedList, ListNode


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int,
                       right: int) -> ListNode:
        """
        Given the head of a singly linked list and 2 indices left and right,
        where left <= right, reverse nodes between (inclusive) left and right

        :param head: The head of the linked list
        :param left: The left index
        :param right: The right index
        :return: The reversed linked list
        """
        if not head:
            return head
        return self.my_soln(head, left, right)

    def my_soln(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Part 1:
        Keep reference to the left_last node

        Part 2:
        Reverse the linked list between [left, right]
        Mark left_last.next = curr (and curr will always point to this node)
        1. Keep reference temp of left_last.next (originally reversed list)
        2. Disconnect left_last and temp, and connect left_last with curr.next
        3. Now left_last.next = curr.next, disconnect curr with its next, and
           connect it with curr.next.next (skips 1)
        4. left_last.next is now the newest reversed node, connect this node to
           the originally reversed list (left_last.next.next = temp)

        Runtime: O(n)
        Space: O(1)
        """
        dummy = ListNode(-1)
        dummy.next = head
        left_last = dummy
        for _ in range(left - 1):
            left_last = left_last.next

        curr = left_last.next
        for _ in range(right - left):
            temp = left_last.next
            left_last.next = curr.next
            curr.next = curr.next.next
            left_last.next.next = temp

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = LinkedList([1, 2, 3, 4, 5]).get_head()
    input2 = 2
    input3 = 4
    expected = LinkedList([1, 4, 3, 2, 5]).get_head()
    actual = Solution().reverseBetween(input1, input2, input3)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = LinkedList([5]).get_head()
    input2 = 1
    input3 = 1
    expected = LinkedList([5]).get_head()
    actual = Solution().reverseBetween(input1, input2, input3)
    print("Test case 2")
    print(actual)
    print(expected)
