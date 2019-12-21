from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given an array of non-negative integers, you are initially positioned at the first index
        of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        Note:
        - You can assume that you can always reach the last index.

        >>> Solution().jump([2, 3, 1, 1, 4])
        2
        >>> Solution().jump([2, 1])
        1

        :param nums: the numbers of steps allowed at each index
        :return: the minimum numbers needed to reach the end of the list
        """
        if len(nums) <= 1:
            return 0
        return self.greedy_soln(nums)

    def greedy_soln(self, nums: List[int]) -> int:
        """
        T: O()
        The greedy solution

        :param nums: the numbers of steps allowed at each index
        :return: the minimum numbers needed to reach the end of the list
        """
        start, end, steps = 0, 0, 0
        while end < len(nums) - 1:
            steps += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return steps
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end
        return steps

    def bfs_soln(self, nums: List[int]) -> int:
        """
        T: O()
        The bfs

        :param nums: the numbers of steps allowed at each index
        :return: the minimum numbers needed to reach the end of the list
        """
        queue = [[0]]
        min_steps = -1
        while queue:
            curr_path = queue.pop()
            if curr_path[-1] == len(nums) - 1:
                if min_steps == -1 or len(curr_path) - 1 < min_steps:
                    min_steps = len(curr_path) - 1
            else:
                available_steps = nums[curr_path[-1]]
                for i in range(1, available_steps + 1):
                    if curr_path[-1] + i < len(nums):
                        queue.insert(0, curr_path + [curr_path[-1] + i])
        return min_steps


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
