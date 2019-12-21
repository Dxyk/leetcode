import collections
from typing import Dict, List, Tuple

from sympy import Interval


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given a collection of intervals, merge all overlapping intervals.

        >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> Solution().merge([[1, 4], [4, 5]])
        [[1, 5]]
        >>> Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])
        [[1, 10]]

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """
        if not intervals or not intervals[0]:
            return []
        return self.sort_soln(intervals)

    def sort_soln(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T: O(nlogn)
        https://leetcode.com/articles/merge-intervals
        Intuition:
        If we sort the intervals according to their start time, then all intervals that can be merged
        will appear to be contiguous
        Algorithm:
        1. Sort the list according to their start time
        2. Insert the first interval to the result list and for each interval,
            a. If current.start > merged.end, then they can be merged
            b. Else they do overlap. update merged.end if necessary
        3.

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for curr in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < curr[0]:
                merged.append(curr)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], curr[1])

        return merged

    def graph_soln(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T: O(n^2)
        https://leetcode.com/articles/merge-intervals
        Intuition:
        A disjoint undirected graph:
            Node: intervals
            Edge: exist if two intervals overlap
        Then all connected nodes can be merged
        Algorithm:
        1. build graph as dict [each node : list of nodes that are overlapping with it]
        2. DFS traverse the graph and get each component of the graph
        3. merge each connected component

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """

        def overlap(a: Interval, b: Interval) -> bool:
            """
            Returns true if the two intervals overlap

            :param a: interval a
            :param b: interval b
            :return: true if a and b overlap
            """
            return a.start <= b.end and b.start <= a.end

        # generate graph where
        def build_graph(interval_list: List[Interval]) -> Dict[Interval, List[Interval]]:
            """
            Build the graph where there is an undirected edge between intervals
            u and v iff u and v overlap.

            To represent the undirected edge, we use each interval as key and the value will be all
            the intervals that are connected to it

            :param interval_list: the list of intervals
            :return: the undirected graph representation of all the intervals
            """
            graph = collections.defaultdict(list)

            # O(n^2)
            for i, curr_interval in enumerate(interval_list):
                for _, target_interval in enumerate(interval_list[i + 1:]):
                    if overlap(curr_interval, target_interval):
                        graph[curr_interval].append(target_interval)
                        graph[target_interval].append(curr_interval)
            return graph

        def merge_nodes(nodes: List[Interval]) -> Interval:
            """
            Merges all of the nodes in this connected component into one interval.

            :param nodes: a list of intervals
            :return: the merged intervals
            """
            min_start = min(node.start for node in nodes)
            max_end = max(node.end for node in nodes)
            return Interval(min_start, max_end)

        def get_components(graph: Dict[Interval, List[Interval]],
                           intervals: List[Interval]) -> Tuple[Dict[int, List[Interval]], int]:
            """
            Gets the dictionary of components.
            Key: arbitrary number; Value: List of Intervals that are connected

            :param graph: the graph of all directed connected intervals
            :param intervals: the list of all intervals
            :return: the unduplicated connected intervals
            """
            visited = set()
            comp_number = 0
            nodes_in_comp = collections.defaultdict(list)

            def mark_component_dfs(start: Interval) -> None:
                """
                DFS traverse the connected Intervals and mark traversed as visited

                :param start: the starting interval
                """
                stack = [start]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        nodes_in_comp[comp_number].append(node)
                        stack.extend(graph[node])

            # mark all nodes in the same connected component with the same integer.
            for interval in intervals:
                if interval not in visited:
                    mark_component_dfs(interval)
                    comp_number += 1

            return nodes_in_comp, comp_number

        intervals = [Interval(l[0], l[1]) for l in intervals]
        graph = build_graph(intervals)
        nodes_in_comp, number_of_comps = get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        merged_intervals = [merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
        return [[interval.start, interval.end] for interval in merged_intervals]

    def brute_force_soln(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T: O(n^2)

        There are four ways two intervals A and B can be merged:
        1.      |----------|        ->      |     ----------|
            |----------|            ->      |----------     |
            A[start] >= B[start] and A[end] >= B[end]   =>  [B[start], A[end]]
        2.      |----------|        ->      |----------   |
                    |----------|    ->      |   ----------|
            A[start <= B[start] and A[end] <= B[end]    =>  [A[start], B[end]]
        3.      |----------|        ->      |----------|
                 |--------|         ->      | -------- |
            A[start] <= B[start] and A[end] >= B[end]   =>  [A[start], A[end]
        4.      |----------|        ->      | ---------- |
               |------------|       ->      |------------|
            A[start] >= B[start] and A[end] <= B[end]   =>  [B[start], B[end]]

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """
        res = []
        intervals.sort(key=lambda x: x[0])  # T: O(nlogn)

        while intervals:  # O(n)
            curr = intervals[0]
            j = 1
            while j < len(intervals):  # T: O(n)
                target = intervals[j]
                if target[0] <= curr[0] <= target[1] <= curr[1]:
                    curr = [target[0], curr[1]]
                    intervals.pop(j)
                elif curr[0] <= target[0] <= curr[1] <= target[1]:
                    curr = [curr[0], target[1]]
                    intervals.pop(j)
                elif curr[0] <= target[0] and curr[1] >= target[1]:
                    curr = [curr[0], curr[1]]
                    intervals.pop(j)
                elif curr[0] >= target[0] and curr[1] <= target[1]:
                    curr = [target[0], target[1]]
                    intervals.pop(j)
                else:
                    j += 1
            res.append(curr)
            intervals.pop(0)

        return res


if __name__ == '__main__':
    Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])
