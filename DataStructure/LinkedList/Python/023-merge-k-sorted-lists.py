from typing import List

from DataStructure.LinkedList.Python.LinkedListDefinitions import LinkedList, ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Merge k sorted LinkedLists into one sorted LinkedList

        >>> lists = [LinkedList([1, 4, 5]).get_start(), LinkedList([1, 3, 4]).get_start(), LinkedList([2, 6]).get_start()]
        >>> str(Solution().mergeKLists(lists))
        '1->1->2->3->4->4->5->6'

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        return self.brute_force(lists)

    def brute_force(self, lists: List[ListNode]) -> ListNode:
        """
        T: O()
        The brute force solution

        :param lists: k sorted linked lists
        :return: 1 sorted linked list
        """
        # TODO