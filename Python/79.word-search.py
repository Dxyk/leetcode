#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (33.12%)
# Likes:    2544
# Dislikes: 133
# Total Accepted:    367.1K
# Total Submissions: 1.1M
# Testcase Example:
#       [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#       "ABCCED"
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#

# @lc code=start
from typing import List, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs_soln(board, word)

    def dfs_soln(self, board: List[List[str]], word: str) -> bool:
        """
        DFS solution
        """
        import copy

        if len(board) == 0 or len(board[0]) == 0:
            return word == ""

        board_cpy = copy.deepcopy(board)
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(substring, i, j):
            if substring == "":
                return True
            if i < 0 or i == len(board_cpy) or \
                    j < 0 or j == len(board_cpy[0]) or \
                    visited[i][j] or substring[0] != board_cpy[i][j]:
                return False
            visited[i][j] = True
            res = dfs(substring[1:], i + 1, j) or \
                dfs(substring[1:], i - 1, j) or \
                dfs(substring[1:], i, j - 1) or \
                dfs(substring[1:], i, j + 1)
            visited[i][j] = False
            return res

        for i in range(len(board_cpy)):
            for j in range(len(board_cpy[i])):
                if dfs(word, i, j):
                    return True
        return False

    def backtrack_soln(self, board: List[List[str]], word: str) -> bool:
        """
        Back tracking solution

        NOTE: This takes too long. See DFS for improved solution
        """
        import copy

        if len(board) == 0 or len(board[0]) == 0:
            return word == ""

        board_cpy = copy.deepcopy(board)

        def backtrack_helper(substring: str,
                             prev_indices: Optional[List[int]]) -> bool:
            if substring == "":
                return True
            start = substring[0]
            i, j = prev_indices
            up_check = down_check = left_check = right_check = False
            if i > 0 and board_cpy[i - 1][j] == start:
                board_cpy[i - 1][j] = ""
                up_check = backtrack_helper(substring[1:], [i - 1, j])
                board_cpy[i - 1][j] = start
            if i < len(board_cpy) - 1 and board_cpy[i + 1][j] == start:
                board_cpy[i + 1][j] = ""
                down_check = backtrack_helper(substring[1:], [i + 1, j])
                board_cpy[i + 1][j] = start
            if j > 0 and board_cpy[i][j - 1] == start:
                board_cpy[i][j - 1] = ""
                left_check = backtrack_helper(substring[1:], [i, j - 1])
                board_cpy[i][j - 1] = start
            if j < len(board_cpy[0]) - 1 and \
                    board_cpy[i][j + 1] == start:
                board_cpy[i][j + 1] = ""
                right_check = backtrack_helper(substring[1:], [i, j + 1])
                board_cpy[i][j + 1] = start
            return up_check or down_check or left_check or right_check

        start = word[0]
        for i in range(len(board_cpy)):
            for j in range(len(board_cpy[i])):
                if board_cpy[i][j] == start:
                    board_cpy[i][j] = ""
                    if backtrack_helper(word[1:], [i, j]):
                        return True
                    board_cpy[i][j] = start
        return False


# @lc code=end


if __name__ == "__main__":
    b = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(Solution().exist(b, "ABCCED"), True)
    print(Solution().exist(b, "SEE"), True)
    print(Solution().exist(b, "ABCB"), False)

    b = [["a", "b"], ["c", "d"]]
    print(Solution().exist(b, "abcd"), False)
