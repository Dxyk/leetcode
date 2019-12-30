#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (34.48%)
# Likes:    1962
# Dislikes: 157
# Total Accepted:    261.9K
# Total Submissions: 757.4K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which
# represents the position (0-indexed) in the linked list where tail connects
# to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#
#
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
#
#
#
# Follow-up:
# Can you solve it without using extra space?
#
#


class ListNode:
    # Definition for singly-linked list.
    # NOTE: LC has its own implementation of ListNode.
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return self.two_pointer_soln(head)

    def two_pointer_soln(self, head: ListNode) -> ListNode:
        """
        Two pointer solution

        Keep two pointers fast and slow
        TODO: Understand this
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if there is a cycle
            if slow == fast:
                # slow2 and slow nodes move step by step
                slow2 = head
                while slow2:
                    if slow2 == slow:
                        return slow2
                    slow2 = slow2.next
                    slow = slow.next
        return None

    def hashset_soln(self, head: ListNode) -> ListNode:
        """
        Hashset solution

        Runtime: O(n)
        Space: O(n)
        """
        seen = set()
        curr = head
        while curr is not None and curr not in seen:
            seen.add(curr)
            curr = curr.next
        return curr

# @lc code=end


if __name__ == "__main__":
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    print(Solution().detectCycle(node).val, 2)

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = node
    print(Solution().detectCycle(node).val, 1)

    node = ListNode(1)
    print(Solution().detectCycle(node), None)
