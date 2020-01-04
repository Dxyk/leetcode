#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (58.45%)
# Likes:    3280
# Dislikes: 78
# Total Accepted:    777.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#

from typing import List


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(lst: List[int]) -> ListNode:
    dummy = ListNode(-1)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def get_list(node: ListNode) -> List[int]:
    curr = node
    res = []
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    return res

# @lc code=start


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursive_soln(head)

    def recursive_soln(self, head: ListNode) -> ListNode:
        """
        Recursive solution
        """
        def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
            if node is None:
                return prev
            next_node = node.next
            node.next = prev
            return reverse(next_node, node)
        return reverse(head)

    def iterative_soln(self, head: ListNode) -> ListNode:
        """
        iterative solution

        Runtime: O(n)
        Space: O(n)
        """
        prev = None
        while head is not None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def bf_soln(self, head: ListNode) -> ListNode:
        """
        BF solution

        Runtime: O(n)
        Space: O(n)
        """
        curr = head
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        dummy = ListNode(-1)
        curr = dummy
        for i in range(len(lst) - 1, -1, -1):
            curr.next = ListNode(lst[i])
            curr = curr.next
        return dummy.next
# @lc code=end


if __name__ == "__main__":
    node = create_list([1, 2, 3, 4, 5])
    print(get_list(Solution().reverseList(node)), [5, 4, 3, 2, 1])
