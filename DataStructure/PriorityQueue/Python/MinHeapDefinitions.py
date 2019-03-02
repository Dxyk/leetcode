from typing import List, TypeVar

T = TypeVar('T')


class MinHeap:
    """
    Idea: Traverse a Tree using a List representation and some simple mathematical operations

    Structure:
    - Complete Binary Tree.
    - Can be represented by an array.
        - Node at index `p`, left child at `2p` and right child at `2p+1`
        - Node at index `n`, parent at `n/2`
    - Min Heap: ForAll node x in the heap, x.parent < x
    - Max Heap: ForAll node x in the heap, x.parent > x

    Operations:
    - Construct: Time: O(1); Space: O(1)
        - Init an empty list
    - Get Min: Time: O(1); Space: O(1)
        - The first element in the heap is the minimum element according to heap's order.
    - Insert: Time: O(Logn); Space: O(n)
        - Append item at end of list (maintains complete tree property)
        - Compare with parent. If smaller than parent, swap. (maintains heap order)
        - Percolate the item upwards
    - Pop Min: Time: O(Logn); Space: O(n)
        - Remove the root of the heap
        - Move the last element to the root (maintains complete tree property)
        - Compare with child. If greater than any one of them, swap (maintains heap order)
        - Percolate the item downwards
    - Build Heap / Heapify: T: O(n); Space: O(n)
        - Build the heap by percolating the elements downwards
        - Note: we percolate from the middle of the list (the last element in the second-last-layer)
    """

    _heap_list: List[T]
    _current_size: int

    def __init__(self):
        # Put a 0 in the list in constructor
        # so that simple integer division can be used in later methods
        self._heap_list = [0]
        self._current_size = 0

    def get_min(self) -> int:
        """
        T: O(1)
        Get the minimum item in the heap

        :return: the minimum item in the heap
        """
        return self._heap_list[1]

    def insert(self, k: T) -> None:
        """
        T: O(Logn)
        Insert an element into the heap

        :param k: the item to insert into the heap
        :return: None
        """
        self._heap_list.append(k)
        self._current_size += 1
        self._perc_up(self._current_size)

    def pop_min(self) -> T:
        """
        T: O(Logn)
        Pop the min item in the heap

        :return: the min item in the heap
        """
        min_val = self._heap_list[1]  # The first element is a dummy
        self._heap_list[1] = self._heap_list[self._current_size]
        self._current_size -= 1
        self._heap_list.pop()
        self._perc_down(1)
        return min_val

    def build_heap(self, lst: List[T]) -> None:
        """
        T: O(n)
        Build a heap with a given list
        Instead of initing empty and inserting one by one (O(nlogn)),
        we perc down each element (O(n)).
        See proof in https://www.growingwiththeweb.com/data-structures/binary-heap/build-heap-proof/

        :param lst: the list of items to build off of
        :return: None
        """
        i = len(lst) // 2
        self._current_size = len(lst)
        self._heap_list = [0] + lst[:]
        while i > 0:
            self._perc_down(i)
            i -= 1

    def get_heap_list(self) -> List[T]:
        """
        Return the heap list

        :return: the heap list
        """
        return self._heap_list[:]

    """
    #############################
    ## PRIVATE METHODS START HERE
    #############################
    """

    def _perc_up(self, i: int):
        """
        T: O(Logn)
        Percolate an item at index i upwards to maintain the heap order

        :param i: the index of the element to percolate up
        :return: None
        """
        while self._get_parent_idx(i) > 0:
            parent_idx = self._get_parent_idx(i)
            if self._heap_list[i] < self._heap_list[parent_idx]:
                # if x < x.parent, swap
                temp = parent_idx
                self._heap_list[parent_idx] = self._heap_list[i]
                self._heap_list[i] = temp
            i //= 2

    def _perc_down(self, i: int) -> None:
        """
        T: O(Logn)
        Percolate an item at index i downwards to maintain the heap order

        :param i: the index of the item to percolate down
        :return: None
        """
        while (i * 2) <= self._current_size:
            min_child_idx = self._get_min_child_idx(i)
            if self._heap_list[i] > self._heap_list[min_child_idx]:
                temp = self._heap_list[i]
                self._heap_list[i] = self._heap_list[min_child_idx]
                self._heap_list[min_child_idx] = temp
            i = min_child_idx

    def _get_parent_idx(self, i: int) -> int:
        """
        T: O(1)
        Get the parent of a node at index i

        :param i: the index of the current node
        :return: the parent index
        """
        return (i - 1) // 2

    def _get_min_child_idx(self, i: int) -> int:
        """
        T: O(1)
        Get the child with minimum value

        :param i: the index of the current node
        :return: the minimum child's index
        """
        if i * 2 + 1 > self._current_size:  # if there is only one child (the last index)
            return i * 2
        else:
            left_idx, right_idx = i * 2, i * 2 + 1
            return left_idx if self._heap_list[left_idx] < self._heap_list[right_idx] else right_idx


if __name__ == '__main__':
    import random

    heap = MinHeap()
    heap.build_heap([random.randint(1, 100) for i in range(100)])
    print(heap.get_heap_list())

