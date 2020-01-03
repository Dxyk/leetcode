#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (36.91%)
# Likes:    2741
# Dislikes: 286
# Total Accepted:    379.5K
# Total Submissions: 1M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
#
# For example, the following two linked lists:
#
#
# begin to intersect at node c1.
#
#
#
# Example 1:
#
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected
# node in B.
#
#
#
# Example 2:
#
#
#
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes
# before the intersected node in A; There are 1 node before the intersected
# node in B.
#
#
#
#
# Example 3:
#
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of
# B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must
# be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
#
# Notes:
#
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked
# structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#

from typing import List, Tuple


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


def create_lists(list_a: List[int], list_b: List[int], skip_a: int,
                 skip_b: int) -> Tuple[ListNode]:
    dummy_a = ListNode(-1)
    curr_a = dummy_a
    for val in list_a[:skip_a]:
        curr_a.next = ListNode(val)
        curr_a = curr_a.next
    dummy_b = ListNode(-1)
    curr_b = dummy_b
    for val in list_b[:skip_b]:
        curr_b.next = ListNode(val)
        curr_b = curr_b.next
    for val in list_a[skip_a:]:
        temp = ListNode(val)
        curr_a.next = temp
        curr_b.next = temp
        curr_a = curr_a.next
        curr_b = curr_b.next
    return dummy_a.next, dummy_b.next
# @lc code=start


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        return self.two_pointer_soln(headA, headB)

    def two_pointer_soln(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Two pointer solution

        Idea:
        Let pointer_a and pointer_b loop through list_a and list_b
        If pointer_a reaches the end of list_a, redirect to head of list_b
        same for pointer_b
        When pointer_a intersects pointer_b, there is the intersect

        Proof:
        Assume list_a of length n, list_b of length m and n < m
        Then pointer_b traverse m-n more node than pointer_a
        after redirecting, pointer_b traverse m-n less node than pointer_a
        So they are gauranteed to meet at intersection node

        Runtime: O(n)
        Space: O(1)
        """
        if headA is None or headB is None:
            return None

        curr_a = headA
        curr_b = headB

        while curr_a != curr_b:
            if curr_a is None:
                curr_a = headB
            else:
                curr_a = curr_a.next
            if curr_b is None:
                curr_b = headA
            else:
                curr_b = curr_b.next

        return curr_a

    def hash_set_soln(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Hash set solution

        Runtime: O(n)
        Space: O(n)
        """
        if headA is None or headB is None:
            return None
        curr_a = headA
        seen = set()
        while curr_a is not None:
            seen.add(curr_a)
            curr_a = curr_a.next
        curr_b = headB
        while curr_b is not None:
            if curr_b in seen:
                return curr_b
            curr_b = curr_b.next
        return None

    def bf_soln(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        BF solution

        Runtime: O(n^2)
        Space: O(1)
        """
        if headA is None or headB is None:
            return None
        curr_a = headA
        while curr_a is not None:
            curr_b = headB
            while curr_b is not None:
                if curr_b == curr_a:
                    return curr_b
                curr_b = curr_b.next
            curr_a = curr_a.next
        return None

# @lc code=end


if __name__ == "__main__":
    node_a, node_b = create_lists([4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3)
    print(Solution().getIntersectionNode(node_a, node_b).val, 8)

    node_a, node_b = create_lists([0, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    print(Solution().getIntersectionNode(node_a, node_b).val, 2)

    node_a, node_b = create_lists([2, 6, 4], [1, 5], 3, 2)
    print(Solution().getIntersectionNode(node_a, node_b), None)
