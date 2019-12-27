#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (48.86%)
# Likes:    2374
# Dislikes: 90
# Total Accepted:    238.9K
# Total Submissions: 488.2K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        return self.dp_soln(n)

    def dp_soln(self, n: int) -> int:
        """
        DP recursive solution

        Let P(n) := number of unique BSTs that can be constructed using
            numbers 1...n
        Let Q(i, n) := number of unique BSTs that can be constructed using
            numbers 1...n with i as the root

        Get P(n) by using each number as root
                P(n) = sum(Q(i, n) for i in 1...n)

        However, using i as root, there are P(i - 1) ways to construct the left
            subtree and P(n - i) ways to construct the right subtree
                Q(i, n) = P(i - 1) * P(n - i)

        Combining those two,
                P(n) = P(0) * P(n - 1) + P(1) * P(n - 2) + ... + P(n-1) * P(0)

        We build the memo from 0 to n because P(n) depends on P(n - 1) to P(0)
        """
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                memo[i] += memo[j - 1] * memo[i - j]
        return memo[n]
# @lc code=end


if __name__ == "__main__":
    print(Solution().numTrees(3), 5)
    print(Solution().numTrees(2), 2)
