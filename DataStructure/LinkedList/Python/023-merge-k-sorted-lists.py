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
        return self.dummy_brute_force(lists)

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
        k: num of lists; n: max num of elements in a list
        T: O(nk^2); S: O(nk)
        The brute force solution

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        result_list_dummy = ptr = ListNode(-1)
        while not all(ll is None for ll in lists):  # O(kn)
            curr_batch = [ll.val for ll in lists if ll is not None]  # O(k)
            curr_min = min(curr_batch)
            for ll in lists:
                if ll is not None and ll.val == curr_min:
                    lists.remove(ll)
                    ll = ll.next
                    lists.append(ll)
                    break
            ptr.next = ListNode(curr_min)
            ptr = ptr.next

        return result_list_dummy.next
