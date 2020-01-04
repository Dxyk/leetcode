#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.04%)
# Likes:    3769
# Dislikes: 137
# Total Accepted:    507.3K
# Total Submissions: 1.1M
# Testcase Example:
#   '[["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#

# @lc code=start
from typing import List


class UF:
    def __init__(self, grid: List[List[str]]):
        self.parents = [-1 for _ in range(len(grid) * len(grid[0]))]
        self.sizes = [1 for _ in range(len(grid) * len(grid[0]))]
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.count += 1
                    lst_coord = i * len(grid[0]) + j
                    self.parents[lst_coord] = lst_coord
        return

    def find(self, coord: int) -> int:
        root_coord = coord
        while root_coord != self.parents[root_coord]:
            root_coord = self.parents[root_coord]
        while coord != root_coord:
            temp = self.parents[coord]
            self.parents[coord] = root_coord
            coord = temp
        return root_coord

    def union(self, coord1: int, coord2: int) -> None:
        root1 = self.find(coord1)
        root2 = self.find(coord2)
        if root1 == root2:
            return
        if self.sizes[root1] >= self.sizes[root2]:
            self.parents[root2] = root1
            self.sizes[root1] += self.sizes[root2]
        else:
            self.parents[root1] = root2
            self.sizes[root2] += self.sizes[root1]
        self.count -= 1
        return


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.union_find_soln(grid)

    def union_find_soln(self, grid: List[List[str]]) -> int:
        """
        Union Find solution
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        uf = UF(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    coord1 = i * len(grid[0]) + j
                    if i < len(grid) - 1 and grid[i + 1][j] == "1":
                        coord2 = (i + 1) * len(grid[0]) + j
                        uf.union(coord1, coord2)
                    if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
                        coord2 = i * len(grid[0]) + j + 1
                        uf.union(coord1, coord2)
        return uf.count

    def dfs_soln(self, grid: List[List[str]]) -> int:
        """
        DFS solution
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def erase_1s(row: int, col: int) -> None:
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) \
                    or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            erase_1s(row - 1, col)
            erase_1s(row + 1, col)
            erase_1s(row, col - 1)
            erase_1s(row, col + 1)
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    erase_1s(i, j)
        return count

    def bfs_soln(self, grid: List[List[str]]) -> int:
        """
        BFS solution
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        offsets = (0, 1, 0, -1, 0)
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    todo = []
                    todo.insert(0, (i, j))
                    grid[i][j] = "0"
                    while len(todo) != 0:
                        curr = todo.pop()
                        for k in range(len(offsets) - 1):
                            r = curr[0] + offsets[k]
                            c = curr[1] + offsets[k + 1]
                            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) \
                                    and grid[r][c] == "1":
                                grid[r][c] = "0"
                                todo.insert(0, (r, c))
        return count

# @lc code=end


if __name__ == "__main__":
    g = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(g), 1)

    g = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(g), 3)

    g = [["1"], ["1"]]
    print(Solution().numIslands(g), 1)
