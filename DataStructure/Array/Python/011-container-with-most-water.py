from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.

        Note: You may not slant the container and n is at least 2.

        >>> Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49

        :type heights: List[int]
        :rtype: int
        """
        if len(heights) < 2:
            return 0
        """ Brute force: O(n^2) """
        # max_area = 0
        # for i in range(len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         min_height = min(heights[i], heights[j])
        #         max_area = max(max_area, min_height * (j - i))
        # return max_area
        """ 
        Sliding window: O(n)
        set left and right pointers. let the lower height shift to the middle
        """
        left_idx, right_idx = 0, len(heights) - 1
        max_area = 0
        while left_idx != right_idx:
            left_height, right_height = heights[left_idx], heights[right_idx]
            new_area = (right_idx - left_idx) * min(left_height, right_height)
            max_area = max(max_area, new_area)

            if left_height < right_height:
                left_idx += 1
            else:
                right_idx -= 1
        return max_area



def main():
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    main()
