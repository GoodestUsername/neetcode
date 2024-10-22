from calendar import c
from collections import defaultdict
from re import L
from typing import List
import unittest
import sys

sys.tracebacklimit = 0

# k = 2
# max_substr = 0
# l = 0

# distance = defaultdict(int)
# for r in range(len(s)):
#     distance[s[r]] += 1
#     max_substr = max(max_substr, r - l + 1)

#     if (r - l + 1) - max_substr > k:
#         distance[s[l]] -= 1
#         l += 1
# AAABBB, k = 3
# ABCAAD, k = 3


# return max(max_substr, r - l + 1)
class Solution:
    def run(self, s: str, k: int) -> int:
        max_substr = 0
        replacements = defaultdict(int)

        for i in range(len(s)):
            cur_char = s[i]
            l = 0
            for r in range(0, len(s)):
                if s[r] != cur_char:
                    replacements[cur_char] += 1
                while replacements[cur_char] > k:
                    if s[l] != cur_char:
                        replacements[cur_char] -= 1
                    l += 1

                max_substr = max(max_substr, r - l + 1)

        return max_substr


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def test_multi(self):
        self.e(args=dict(s="XYYX", k=2), expected=4)

    def test_single(self):
        self.e(args=dict(s="AAABABB", k=1), expected=5)

    def test_odd_len(self):
        self.e(args=dict(s="AABABBA", k=1), expected=4)

    def test_same_distance_middle(self):
        self.e(args=dict(s="ABBA", k=2), expected=4)

    def test_false_start(self):
        self.e(args=dict(s="ABBB", k=2), expected=4)

    def test_rep_pattern(self):
        self.e(args=dict(s="ABAB", k=2), expected=4)


if __name__ == "__main__":
    unittest.main()

    # substr = ""
    # keep adding more chars until hit duplicate char
    # on hit duplicate char
    # look for first appearance of dup char
    # -  if first char is dup, pop and continue
    # compare max substr on dup hit or end of loop


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res
