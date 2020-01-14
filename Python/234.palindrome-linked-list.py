#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (37.53%)
# Likes:    2284
# Dislikes: 309
# Total Accepted:    336.9K
# Total Submissions: 893.7K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head: ListNode) -> bool:
        return self.two_pointer_soln(head)

    def two_pointer_improved(self, head: ListNode) -> bool:
        """
        Two pointer improved solution

        Runtime: O(n)
        Space: O(n)
        """
        rev = None
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next

        if fast is not None:
            tail = head.next
        else:
            tail = head

        is_palindrome = True
        while rev:
            is_palindrome = is_palindrome and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return is_palindrome

    def two_pointer_soln(self, head: ListNode) -> bool:
        """
        Two pointer solution

        Runtime: O(n)
        Space: O(n)
        """
        slow = fast = head
        rev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            # rev, rev.next, slow = slow, rev, slow.next
            temp_rev = rev
            rev = slow
            slow = slow.next
            rev.next = temp_rev
        if fast is not None:
            slow = slow.next
        while rev is not None and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return rev is None

    def bf_soln(self, head: ListNode) -> bool:
        """
        BF solution

        Runtime: O(n)
        Space: O(n)
        """
        lst = []
        curr = head
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        mid = len(lst) // 2
        mid_prev = mid - 1 if len(lst) % 2 == 0 else mid
        return lst[: mid] == lst[-1: mid_prev: -1]
# @lc code=end


if __name__ == "__main__":
    node = create_list([1, 2])
    print(Solution().isPalindrome(node), False)
    node = create_list([1])
    print(Solution().isPalindrome(node), True)
    node = create_list([0, 0])
    print(Solution().isPalindrome(node), True)
    node = create_list([1, 2, 1])
    print(Solution().isPalindrome(node), True)
    node = create_list([1, 2, 2, 1])
    print(Solution().isPalindrome(node), True)
