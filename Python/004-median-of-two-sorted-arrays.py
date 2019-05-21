from typing import List


class Solution:

    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        """
        There are two _sorted_ arrays A and B of size m and n respectively.

        Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

        You may assume A and B cannot be both empty.

        >>> Solution().findMedianSortedArrays([1, 3], [2])  # [1, 2, 3]
        2
        >>> Solution().findMedianSortedArrays([1, 2], [3, 4])  # [1, 2, 3, 4] -> (2 + 3) / 2 = 2.5
        2.5

        :param A: a list of sorted ints
        :type A: List[int]
        :param B: a list of sorted ints
        :type B: List[int]
        :return: the median of the two lists combined
        :rtype: float
        """
        """ Brute Force: O(m + n) """
        # C is a sorted list of {A, B}
        # C = []
        # m, n = len(A), len(B)
        # while m > 0 or n > 0:
        #     if m > 0 and n > 0:
        #         if A[0] <= B[0]:
        #             C.append(A[0])
        #             A.remove(A[0])
        #         else:
        #             C.append(B[0])
        #             B.remove(B[0])
        #     elif m > 0:
        #         C.append(A[0])
        #         A.remove(A[0])
        #     elif n > 0:
        #         C.append(B[0])
        #         B.remove(B[0])
        # total_size = len(C)
        # if total_size % 2 == 0:
        #     return (C[total_size // 2 - 1] + C[total_size // 2]) / 2
        # else:
        #     return C[total_size // 2]

        """
        Binary Search: O(log(min(m, n)))
        Let i in [0, m) and j in [0, n) separate A, B
        Let the median of {A, B} = max(i, j). 
        Then for all a in A[: i - 1] < for all a' in A[i:]
        Then for all b in B[: j - 1] < for all b' in B[j:]  
        Then i, j must satisfy [ i + j = m - i + n - j ]  // since median will separate a list in to two equal length parts
        Let i \in [0, m) be arbitrary
        Then $ j = (m + n - 1) / 2 - i $
        
        WTF: i s.t. (i == 0 || j == n || A[i - 1] < B[j]) && 
                    (i == m || j == 0 || A[i] > B[j - 1])
        Use Binary Search to find i
        """

        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        i_min, i_max = 0, m
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = (m + n + 1) // 2 - i

            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                i_min = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                i_max = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


def main():
    ret = Solution().findMedianSortedArrays([1, 3], [2])

    out = str(ret)
    print(out)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
