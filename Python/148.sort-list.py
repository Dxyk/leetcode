#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (38.51%)
# Likes:    1995
# Dislikes: 101
# Total Accepted:    223.2K
# Total Submissions: 577.2K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#

# @lc code=start


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.merge_sort_bottom_up_soln(head)

    def merge_sort_bottom_up_soln(self, head: ListNode) -> ListNode:
        """
        Merge sort bottom up solution

        Runtime: O(nlogn)
        Space: O(1)
        """
        def split(node: ListNode, step: int) -> ListNode:
            i = 1
            while i < step and node is not None:
                node = node.next
                i += 1
            if node is None:
                return None
            temp = node.next
            node.next = None
            return temp

        def merge(node1: ListNode, node2: ListNode,
                  node: ListNode) -> ListNode:
            curr = node
            while node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next
            if node1 is not None:
                curr.next = node1
            if node2 is not None:
                curr.next = node2
            while curr.next is not None:
                curr = curr.next
            return curr

        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head
        step = 1
        while step < count:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = split(left, step)
                curr = split(right, step)
                tail = merge(left, right, tail)
            step *= 2
        return dummy.next

    def merge_sort_soln(self, head: ListNode) -> ListNode:
        """
        Merge sort solution

        Idea:
        Cut the list in half. Sort when merging

        Runtime: O(nlogn)
        Space: O(logn)
        """
        def merge_sort(node: ListNode):
            if node is None or node.next is None:
                return node
            slow = fast = node
            prev = None
            while fast is not None and fast.next is not None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            node1 = merge_sort(node)
            node2 = merge_sort(slow)
            return merge(node1, node2)

        def merge(node1: ListNode, node2: ListNode) -> ListNode:
            dummy = ListNode(-1)
            curr = dummy
            curr1, curr2 = node1, node2
            while curr1 is not None and curr2 is not None:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                curr = curr.next
            if curr1 is not None:
                curr.next = curr1
            if curr2 is not None:
                curr.next = curr2
            return dummy.next
        return merge_sort(head)

    def bf_soln(self, head: ListNode) -> ListNode:
        """
        Brute force solution

        Idea:
        Add all nodes to list. Sort list and create head

        Runtime: O(nlogn)
        Space: O(n)
        """
        all_val = []
        curr = head
        while curr is not None:
            all_val.append(curr.val)
            curr = curr.next
        all_val.sort()
        dummy = ListNode(-1)
        curr = dummy
        for val in all_val:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
# @lc code=end


if __name__ == "__main__":
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    sorted_node = Solution().sortList(node)
    curr = sorted_node
    res = []
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    print(res)
    print([1, 2, 3, 4])

    node = ListNode(-1)
    node.next = ListNode(5)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(0)
    sorted_node = Solution().sortList(node)
    curr = sorted_node
    res = []
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    print(res)
    print([-1, 0, 3, 4, 5])
