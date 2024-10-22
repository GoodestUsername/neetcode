from collections import defaultdict
from re import X
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, board: List[List[str]]) -> bool:
        valid_nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

        usedDigits: List[dict[str, dict[int, bool]]] = [
            {"x": {}, "y": {}} for _ in range(9)
        ]

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in valid_nums:
                    num = int(board[row][col]) - 1
                    x_coord = usedDigits[num]["y"].get(col, -1)
                    y_coord = usedDigits[num]["x"].get(row, -1)

                    if y_coord != -1 or x_coord != -1:
                        return False

                    base = 0
                    if col >= 6:
                        base = 6
                    elif col >= 3:
                        base = 3

                    range_of_coord = range(base, base + 2)
                    for i in range(base, base + 3):
                        if i == col:
                            continue

                        used_xCoord = usedDigits[num]["x"].get(i, -1)
                        if used_xCoord in range_of_coord:
                            return False

                    usedDigits[num]["x"][row] = col
                    usedDigits[num]["y"][col] = row

                else:
                    return False

        return True


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_no_dup(self):
        self.e(
            args=[
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            expected=True,
        )

    def test_dup(self):
        self.e(
            args=[
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            expected=False,
        )


if __name__ == "__main__":
    unittest.main()

# other
# simplifies the squares 1 dimension down into a 3x3 grid and check against the set of
# used values
# column and row check is same as above
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         cols = defaultdict(set)
#         rows = defaultdict(set)
#         squares = defaultdict(set)  # key = (r /3, c /3)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if (
#                     board[r][c] in rows[r]
#                     or board[r][c] in cols[c]
#                     or board[r][c] in squares[(r // 3, c // 3)]
#                 ):
#                     return False
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])

#         return True
