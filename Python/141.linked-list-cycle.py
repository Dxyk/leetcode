#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (38.99%)
# Likes:    2093
# Dislikes: 310
# Total Accepted:    508.3K
# Total Submissions: 1.3M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
#

# @lc code=start


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.two_pointer_soln(head)

    def two_pointer_soln(self, head: ListNode) -> bool:
        """
        Two pointer solution

        keep a slow and fast pointer. If the slow pointer is at one point at
        the same place as the fast pointer, then there is a cycle

        Runtime: O(n)
        Space: O(1)
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def bf_soln(self, head: ListNode) -> bool:
        """
        BF solution by keeping a set of all seen nodes

        Runtime: O(n)
        Space: O(n)
        """
        seen = set()
        curr = head
        while curr is not None:
            if curr not in seen:
                seen.add(curr)
            else:
                return True
            curr = curr.next
        return False
# @lc code=end


if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    print(Solution().hasCycle(node), True)

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = node
    print(Solution().hasCycle(node), True)

    node = ListNode(1)
    print(Solution().hasCycle(node), False)
