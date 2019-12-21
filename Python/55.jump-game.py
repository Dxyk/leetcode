from typing import List, Union


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Given an array of non-negative integers, you are initially positioned at the first index
        of the array.

        Each element in the array represents your maximum jump length at that position.

        Determine if you are able to reach the last index.

        >>> Solution().canJump([2, 3, 1, 1, 4])
        True
        >>> Solution().canJump([3, 2, 1, 0, 4])
        False
        >>> Solution().canJump([1, 1, 2, 0, 0])
        True
        >>> Solution().canJump([5, 0, 0, 0, 0])
        True

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """
        if not nums or len(nums) == 1:
            return True
        return self.dp_greedy_soln(nums)

    def my_greedy_soln(self, nums: List[int]) -> bool:
        """
        T: O(n)
        The greedy soln
        traverse the list base on the max steps we can take

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """
        max_step = nums[0]
        for idx in range(1, len(nums)):
            if idx > max_step:
                return False
            max_step = max(idx + nums[idx], max_step)
        return max_step >= len(nums) - 1

    def dp_greedy_soln(self, nums: List[int]) -> bool:
        """
        T: O(n)
        The dp greedy soln.
        We observe from the bottom up solution that:
        We update an idx when we meet the left most idx from it that is true.
        Thus we can only keep track of the left most idx and get rid of the memo

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """
        last_idx = len(nums) - 1
        for idx in range(last_idx - 1, -1, -1):
            if idx + nums[idx] >= last_idx:
                last_idx = idx
        return last_idx == 0

    def dp_bottom_up_soln(self, nums: List[int]) -> bool:
        """
        T: O(n^2)
        The dp bottom up soln.
        We observe that when we update the memo, we do it backwards. Thus we can traverse the memo
        in reverse direction and set an index to True if there is an index between the curr to the
        final idx that is true.

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """
        memo: List[Union[bool, None]] = [None] * len(nums)
        memo[-1] = True

        for pos in range(len(nums) - 1, -1, -1):
            furthest_jump = min(pos + nums[pos], len(nums) - 1)
            for next_pos in range(pos + 1, furthest_jump):
                if memo[next_pos]:
                    memo[pos] = True
                    break
        return memo[0]

    def dp_memoized_soln(self, nums: List[int]) -> bool:
        """
        T: O(n^2)
        Observe from back tracking soln, each recursive calls, we're recomputing if an index at x is
        a good position. We can keep the index - good/bad as memo to reduce time

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """

        def back_track_helper(position: int, nums: List[int],
                              memo: List[Union[bool, None]]) -> bool:
            """
            :param position: The current position
            :param nums: The list of jump distances
            :param memo: The list of memo. True if the idx is a good idx
            :return: True if we can reach the end, False otherwise
            """
            if memo[position] is not None:
                return memo[position]
            furthest_jump = min(position + nums[position], len(nums) - 1)
            for next_pos in range(furthest_jump, position, -1):
                if back_track_helper(next_pos, nums, memo):
                    memo[position] = True
                    return True
            memo[position] = False
            return False

        memo: List[Union[bool, None]] = [None] * len(nums)
        memo[-1] = True
        return back_track_helper(0, nums, memo)

    def back_tracking_soln(self, nums: List[int]) -> bool:
        """
        T: O(2^n)
        The naive back tracking soln
        Look through every possible step. If stuck, backtrack.

        :param nums: The array of jump distances
        :return: True if we can reach the end, False otherwise
        """

        def back_track_helper(position: int, nums: List[int]) -> bool:
            """
            :param position: The current position
            :param nums: The list of jump distances
            :return: True if we can reach the end, False otherwise
            """
            if position == len(nums) - 1:
                return True
            furthest_jump = min(position + nums[position], len(nums) - 1)
            for next_pos in range(furthest_jump, position, -1):
                if back_track_helper(next_pos, nums):
                    return True
            return False

        return back_track_helper(0, nums)
