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
