#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (40.18%)
# Likes:    2610
# Dislikes: 134
# Total Accepted:    301.1K
# Total Submissions: 747.1K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
# Example 1:
#
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
#
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
#
#
# Note:
#
#
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        return self.bfs_soln(numCourses, prerequisites)

    def bfs_soln(self, num_courses: int,
                 prerequisites: List[List[int]]) -> bool:
        """
        BFS Solution

        Idea:
        Use graph representation. [1, 0] := edge 1 -> 0.
        BFS traverse the graph. If all nodes are traversed without any
        duplicates, then return true.
        """
        graph = {node: set() for node in range(num_courses)}
        out_degrees = {node: 0 for node in range(num_courses)}
        for start, end in set(tuple(x) for x in prerequisites):
            graph[start] |= {end}
            out_degrees[end] += 1

        queue = []
        for node in range(num_courses):
            if out_degrees[node] == 0:
                queue.insert(0, node)

        visited = set(queue)
        while len(queue) != 0:
            node = queue.pop()
            for neighbor in graph[node]:
                if neighbor in visited:
                    return False
                out_degrees[neighbor] -= 1
                if out_degrees[neighbor] == 0:
                    visited.add(neighbor)
                    queue.insert(0, neighbor)
        return len(visited) == num_courses

    def dfs_soln(self, num_courses: int,
                 prerequisites: List[List[int]]) -> bool:
        """
        DFS Solution

        Idea:
        Use graph representation. [1, 0] := edge 1 -> 0.
        Detect if there is a cycle in the directed graph
        """
        graph = [[] for _ in range(num_courses)]
        # States for visited:
        #   0: unvisited
        #   1: _been_ visited. If run into 1, skip it
        #   -1: _being_ visited. If run into -1, then there is a loop
        visited = [0 for _ in range(num_courses)]

        def dfs(node: int) -> bool:
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
            visited[node] = 1
            return True

        for x, y in prerequisites:
            graph[x].append(y)
        for node in range(num_courses):
            if not dfs(node):
                return False
        return True
# @lc code=end


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]), True)
    print(Solution().canFinish(2, [[1, 0], [0, 1]]), False)
