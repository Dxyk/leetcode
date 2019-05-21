from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Given an unsorted integer array, find the smallest missing positive integer.

        >>> Solution().firstMissingPositive([1, 2, 0])
        3
        >>> Solution().firstMissingPositive([3, 4, -1, 1])
        2
        >>> Solution().firstMissingPositive([7, 8, 9, 11, 12])
        1

        :param nums: a list of unsorted integer array
        :return: the smallest missing positive integer
        """
        if not nums:
            return 1
        return self.leet_code_soln(nums)

    def leet_code_soln(self, nums: List[int]) -> int:
        """
        T: O(n)

        Idea:
        for any k positive nums (allow dup), the first missing positive num must be in [1:k+1] in R.
        e.g. k balls into k + 1 bins, there must be a bin that's empty

        Steps:
        1. Since there are 0 and -ive, we partition the list as we do in quick sort and get k
        2. Now nums[:,k] are +ive. Then the first missing number must be in [1:k+1] in R.
           We use nums[i] to indicate whether the number i + 1 exists.
           e.g. nums[0] should be 1
           If nums[i] exists, set it to -ive to indicate that.
        3. Then scan the elements between nums[-:k] to find the first positive element.
           nums[i] +ive => i+1 does not exist

        https://leetcode.com/problems/first-missing-positive/discuss/17073

        :param nums: a list of unsorted integer array
        :return: the smallest missing positive integer
        """
        n = len(nums)

        # Step 1: partition the array
        k = -1
        for i in range(n):
            if nums[i] > 0:
                k += 1
                nums[k], nums[i] = nums[i], nums[k]
        k += 1
        first_missing_idx = k

        # Step 2: if the number exists and is in place, then set it to minus
        for i in range(k):
            temp = abs(nums[i])
            if temp <= k:
                if nums[temp - 1] > 0:
                    nums[temp - 1] *= -1

        # Step 3: scan the list and find the one that's not in place and positive
        for i in range(k):
            if nums[i] > 0:
                first_missing_idx = i
                break

        return first_missing_idx + 1

    def brute_force(self, nums: List[int]) -> int:
        """
        T: O(nlogn)
        The brute force solution:
        Sort the nums list and loop through the list

        :param nums: a list of unsorted integer array
        :return: the smallest missing positive integer
        """
        nums.sort()  # O(nlogn)
        res = 1
        for num in nums:
            if 0 < num == res:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1, 2, 0]))
