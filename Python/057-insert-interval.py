from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Given a set of non-overlapping intervals, insert a new interval into the intervals
        (merge if necessary).

        You may assume that the intervals were initially sorted according to their start times.

        >>> Solution().insert([[1, 3], [6, 9]], [2, 5])
        [[1, 5], [6, 9]]
        >>> Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        [[1, 2], [3, 10], [12, 16]]
        >>> Solution().insert([], [5, 7])
        [[5, 7]]

        :param intervals: the list of intervals
        :param new_interval: the new interval to be inserted into the list
        :return: the resulting intervals
        """
        if not new_interval:
            return intervals
        return self.sliding_soln(intervals, new_interval)

    def sliding_soln(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        T: O(n)
        Slide through each interval. There are two cases
        1. No overlapping and new earlier than curr - keep sliding
        2. Overlapping - the merged result:
           start = min(curr.start, new.start)
           end = max(curr.end, new.end)
        3. No overlapping and new later than curr - we stop here

        :param intervals: the list of intervals
        :param new_interval: the new interval to be inserted into the list
        :return: the resulting intervals
        """
        start = new_interval[0]
        end = new_interval[1]
        res = []

        i = 0
        while i < len(intervals):
            curr = intervals[i]
            if start <= curr[1]:
                if end < curr[0]:
                    break
                else:
                    start = min(start, curr[0])
                    end = max(end, curr[1])
            else:
                res.append(curr)
            i += 1
        res.append([start, end])
        res.extend(intervals[i:])
        return res

    def naive_approach(self, intervals: List[List[int]], new_interval: List[int]) -> List[
        List[int]]:
        """
        T: O(nlogn)
        The naive approach:
        Insert the new interval into the right position and then merge according
        to 056-merge-interval

        :param intervals: the list of intervals
        :param new_interval: the new interval to be inserted into the list
        :return: the resulting intervals
        """
        i = 0
        while i < len(intervals) and intervals[i][0] < new_interval[0]:
            i += 1
        intervals.insert(i, new_interval)

        res = []
        for curr in intervals:
            if not res or res[-1][1] < curr[0]:
                res.append(curr)
            else:
                res[-1][1] = max(res[-1][1], curr[1])

        return res
