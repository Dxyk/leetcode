#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (43.61%)
# Likes:    2310
# Dislikes: 410
# Total Accepted:    279.5K
# Total Submissions: 619.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
#
#
#

from Python.commons.LinkedList import ListNode, LinkedList


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Given the head of a linked list and a value x,
        partition it such that all nodes < x come before
        nodes >= to x.

        The original relative order of the nodes in each
        of the two partitions should be preserved.

        :param head: The head of a linked list to partition
        :param x: The value to partition by
        :return: The partitioned linked list where all nodes < x come before nodes that are >= x
        """
        if not head:
            return head
        return self.two_list(head, x)

    def two_list(self, head: ListNode, x: int) -> ListNode:
        """
        Two List Solution

        Build 2 LinkedLists from scratch (using dummy nodes)
        - head1 are all the nodes that are less than x
            - Use pt1 to keep track of the latest node
        - head2 are all the nodes that are greater than x
            - Use pt2 to keep track of the latest node

        After the 2 LinkedLists are built,
        - Clear the remaining of the pt2, since those are not valid
        - Add head2 to the end of head1 (pt1.next)

        Return head1

        Runtime: O(n)
        Space: O(n)
        """
        head1 = pt1 = ListNode(-1)
        head2 = pt2 = ListNode(-1)
        curr = head

        while curr:
            if curr.val < x:
                pt1.next = curr
                pt1 = pt1.next
            else:
                pt2.next = curr
                pt2 = pt2.next
            curr = curr.next

        pt2.next = None
        pt1.next = head2.next

        return head1.next

    def two_pointer(self, head: ListNode, x: int) -> ListNode:
        """
        Two Pointer Solution
        Less space complexity compared to two_list, but harder to follow

        - prev: last valid node which node.val < x
        - curr: last valid node which node.val >=x
        Use curr.next to perform checks

        If curr.next >= x:
            Nothing to do. Leave prev as is and increment curr
        Else:
            Use temp to keep track of curr.next (we want to move this)
            Update curr.next to curr.next.next (cut the link to temp)
            Update temp.next to prev.next (before linking temp to prev, save reference to prev.next)
            Update prev.next to temp (link temp to prev)
            Increment prev
            Do not increment curr since curr.next is updated

        Edge Case: (the tricky part)
            When the method starts, prev and curr are both at the dummy node
            The curr.next >= x case will work as normal
            The curr.next >= x case won't work and will cause infinite loop
                To deal with this, increment both to head
                prev will be valid, so will curr

        Runtime: O(n)
        Space: O(1)
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev = curr = dummy
        while curr and curr.next:
            if curr.next.val < x:
                if prev == curr:
                    prev = prev.next
                    curr = curr.next
                else:
                    temp = curr.next
                    curr.next = temp.next
                    temp.next = prev.next
                    prev.next = temp
                    prev = prev.next
            else:
                curr = curr.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    # Test Case 1
    input1 = LinkedList([1, 4, 3, 2, 5, 2]).get_start()
    input2 = 3
    expected = LinkedList([1, 2, 2, 4, 3, 5]).get_start()
    actual = Solution().partition(input1, input2)
    print("Test case 1")
    print(actual)
    print(expected)

    # Test Case 2
    input1 = LinkedList([2, 1]).get_start()
    input2 = 2
    expected = LinkedList([1, 2]).get_start()
    actual = Solution().partition(input1, input2)
    print("Test case 1")
    print(actual)
    print(expected)
