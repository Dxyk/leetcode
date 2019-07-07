from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given a collection of intervals, merge all overlapping intervals.

        >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> Solution().merge([[1, 4], [4, 5]])
        [[1, 5]]

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """
        if not intervals or not intervals[0]:
            return []
        return self.brute_force_soln(intervals)

    def brute_force_soln(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T: O()

        There are four ways two intervals A and B can be merged:
        1.      |----------|            ->  |     ----------|
            |----------|                ->  |----------     |
            A[start] >= B[start] and A[end] >= B[end]   =>  [B[start], A[end]]
        2.      |----------|            ->  |----------   |
                    |----------|        ->  |   ----------|
            A[start <= B[start] and A[end] <= B[end]    =>  [A[start], B[end]]
        3.      |----------|            ->  |----------|
                 |--------|             ->  | -------- |
            A[start] <= B[start] and A[end] >= B[end]   =>  [A[start], A[end]
        4.      |----------|            ->  | ---------- |
               |------------|           ->  |------------|
            A[start] >= B[start] and A[end] <= B[end]   =>  [B[start], B[end]]

        :param intervals: a collection of intervals
        :return: a collection of merged intervals
        """
        res = []
        i = 0
        while i < len(intervals):
            curr = intervals[i]
            has_merged = False
            j = i + 1
            while j < len(intervals):
                target = intervals[j]
                if curr[0] >= target[0] and curr[1] >= target[1]:
                    curr = [target[0], curr[1]]
                    intervals.remove(target)
                    has_merged = True
                elif curr[0] <= target[0] and curr[1] <= target[1]:
                    curr = [curr[0], target[1]]
                    intervals.remove(target)
                    has_merged = True
                elif curr[0] <= target[0] and curr[1] >= target[1]:
                    curr = [curr[0], curr[1]]
                    intervals.remove(target)
                    has_merged = True
                elif curr[0] >= target[0] and curr[1] <= target[1]:
                    curr = [target[0], target[1]]
                    intervals.remove(target)
                    has_merged = True
                else:
                    j += 1
            res.append(curr)
            if not has_merged:
                i += 1

        return res
