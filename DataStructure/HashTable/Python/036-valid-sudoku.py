from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.

        Only the filled cells need to be validated according to the following rules:

        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        :param board: a 2D matrix that represents a sudoku board
        :return: true if the sudoku is valid, false otherwise
        """
        return self.hash_table(board)

    def hash_table(self, board: List[List[str]]) -> bool:
        """
        T: O()
        A HashTable solution

        :param board: a 2D matrix that represents a sudoku board
        :return: true if the sudoku is valid, false otherwise
        """
        # a hash table [number : list of coordinates on the board]
        # O(n^2)
        num_to_coord = {str(key): [] for key in range(1, 10)}
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                num = board[row_idx][col_idx]
                if num != '.':
                    num_to_coord[num].append((row_idx, col_idx))

        # find duplicates within each row, each col and each 3*3 block for each number
        # O(n^2)
        for num, coords in num_to_coord.items():
            # rows and cols for a number cannot have duplicates
            rows = [coord[0] for coord in coords]
            cols = [coord[1] for coord in coords]
            if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
                return False

            # check duplicates for every 3 * 3 block
            blocks_tpl = [(coord[0] // 3, coord[1] // 3) for coord in coords]
            if len(blocks_tpl) != len(set(blocks_tpl)):
                return False
        return True

    def brute_force(self, board: List[List[str]]) -> bool:
        """
        T: O(n^4)
        The brute force solution

        :param board: a 2D matrix that represents a sudoku board
        :return: true if the sudoku is valid, false otherwise
        """
        # check rows O(n^3)
        for row in board:  # O(n)
            for curr_idx in range(len(row)):  # O(n)
                curr = row[curr_idx]
                if curr != ".":
                    for compare_idx in range(len(row)):  # O(n)
                        compare = row[compare_idx]
                        if compare_idx != curr_idx and compare != "." and curr == compare:
                            return False

        # check cols O(n^3)
        for idx in range(len(board[0])):
            for curr_row_idx in range(len(board)):
                curr_row = board[curr_row_idx]
                curr = curr_row[idx]
                if curr == ".":
                    continue
                for compare_row_idx in range(len(board)):
                    compare_row = board[compare_row_idx]
                    compare = compare_row[idx]
                    if compare_row_idx != curr_row_idx and compare != "." and curr == compare:
                        return False

        # check 3*3 blocks O(n^4)
        for row_idx in range(0, len(board), 3):  # O(n)
            for col_idx in range(0, len(board[0]), 3):  # O(n)
                curr_block = []
                curr_block.extend(board[row_idx][col_idx: col_idx + 3])
                curr_block.extend(board[row_idx + 1][col_idx: col_idx + 3])
                curr_block.extend(board[row_idx + 2][col_idx: col_idx + 3])
                for curr_idx in range(len(curr_block)):  # O(n)
                    curr = curr_block[curr_idx]
                    if curr == ".":
                        continue
                    for compare_idx in range(len(curr_block)):  # O(n)
                        compare = curr_block[compare_idx]
                        if compare_idx != curr_idx and compare != "." and curr == compare:
                            return False

        return True


if __name__ == '__main__':
    # True example
    b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().isValidSudoku(b))

    # False example
    # Comparing to the example above, only b[0][0] is changed from 5 to 8
    # Then the first col contains 2 8s. Invalid
    b = [['8', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print(Solution().isValidSudoku(b))

    # False example
    b = [['.', '.', '.', '.', '5', '.', '.', '1', '.'],
         ['.', '4', '.', '3', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '3', '.', '.', '1'],
         ['8', '.', '.', '.', '.', '.', '.', '2', '.'],
         ['.', '.', '2', '.', '7', '.', '.', '.', '.'],
         ['.', '1', '5', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
         ['.', '2', '.', '9', '.', '.', '.', '.', '.'],
         ['.', '.', '4', '.', '.', '.', '.', '.', '.']]
    print(Solution().isValidSudoku(b))
