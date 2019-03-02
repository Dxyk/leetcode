from queue import PriorityQueue
from typing import List

from DataStructure.LinkedList.Python.LinkedListDefinitions import LinkedList, ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Merge k sorted LinkedLists into one sorted LinkedList

        >>> lists = [LinkedList([1, 4, 5]).get_start(), LinkedList([1, 3, 4]).get_start(), LinkedList([2, 6]).get_start()]
        >>> str(Solution().mergeKLists(lists))
        '1->1->2->3->4->4->5->6'
        >>> lists = [LinkedList([]).get_start(), LinkedList([1]).get_start()]
        >>> str(Solution().mergeKLists(lists))
        '1'

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        return self.brute_force(lists)

    def divide_and_conquer(self, lists: List[ListNode]) -> ListNode:
        """
        k: num of lists; n: max num of elements in a list
        T: O(kN); S: O(1)
        Similar to merge_one_by_one, but using divide and conquer

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        total = len(lists)
        interval = 1  # the interval between two merging lists
        while interval < total:
            for i in range(0, total - interval, interval * 2):
                lists[i] = self._merge_two_lists_iterative(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if total > 0 else lists

    def merge_one_by_one(self, lists: List[ListNode]) -> ListNode:
        """
        k: num of lists; n: max num of elements in a list
        T: O(kN); S: O(1)
        Merge one by one. See 021-merge-two-sorted-lists

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        if len(lists) > 0:
            result = lists[0]
            for i in range(1, len(lists)):
                result = self._merge_two_lists_iterative(result, lists[i])
            return result

    def _merge_two_lists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T: O(n)

        :param l1: list node 1
        :param l2: list node 2
        :return: the resulting merged list node's head
        """
        if None in (l1, l2):
            return l1 or l2
        result_head_dummy = ptr = ListNode(-1)
        result_head_dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = ptr.next
                ptr.next = l2
                temp = l2.next
                l2.next = nxt
                l2 = temp
            ptr = ptr.next
        # don't need to continue the loop. can just point the head to the list with remaining elements
        ptr.next = l1 or l2
        return result_head_dummy.next

    def priority_queue(self, lists: List[ListNode]) -> ListNode:
        """
        k: num of lists; n: max num of elements in a list
        T: O(N logk); S: O(nk)
        Using a priority queue

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        dummy_head = ptr = ListNode(-1)
        q = PriorityQueue()

        # put all items in the queue (O(k log k))
        for ll in lists:
            if ll:
                q.put((ll.val, ll))

        while not q.empty():
            val, node = q.get()
            ptr.next = ListNode(val)
            ptr = ptr.next
            node = node.next
            if node:
                q.put((node.val, node))

        return dummy_head.next

    def dummy_brute_force(self, lists: List[ListNode]) -> ListNode:
        """
        k: num of lists; n: max num of elements in a list
        T: O(nk^2); S: O(nk)
        The brute force solution: get every node to a list and sort them and create a new ll

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        nodes = []
        dummy_head = ptr = ListNode(-1)

        for ll in lists:  # O(kn)
            while ll is not None:
                nodes.append(ll.val)
                ll = ll.next

        for num in sorted(nodes):  # O(kn log(kn))
            ptr.next = ListNode(num)
            ptr = ptr.next

        return dummy_head.next

    def brute_force(self, lists: List[ListNode]) -> ListNode:
        """
        k: num of lists; n: max num of elements in a list; N: total number of nodes
        T: O(Nk); S: O(nk)
        The brute force solution: compare every first element in the node

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        result_list_dummy = ptr = ListNode(-1)
        while not all(ll is None for ll in lists):  # O(kn)
            curr_batch = [(idx, item) for (idx, item) in enumerate(lists) if
                          item is not None]  # O(k)
            current_min_idx, curr_min_node = min(curr_batch, key=lambda tup: tup[1].val)
            ptr.next = curr_min_node
            ptr = ptr.next
            curr_min_node = curr_min_node.next
            lists[current_min_idx] = curr_min_node

        return result_list_dummy.next
