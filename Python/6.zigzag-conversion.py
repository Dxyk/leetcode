class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
        like this: (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Write the code that will take a string and make this conversion given a number of rows:

        >>> Solution().convert("PAYPALISHIRING", 3)
        "PAHNAPLSIIGYIR"
        >>> Solution().convert("PAYPALISHIRING", 4)
        "PINALSIGYAHRPI"

        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [''] * numRows
        num = (numRows - 1) * 2
        for i, item in enumerate(s):
            if i % num >= numRows:
                rows[(num - i % num) % numRows] += item
            else:
                rows[i % num] += item
        return ''.join(rows)


def main():
    print(Solution().convert("PAYPALISHIRING", 4))


if __name__ == '__main__':
    main()
