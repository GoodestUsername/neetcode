from calendar import c
from collections import defaultdict
from re import L
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, s1: str, s2: str) -> bool:
        s1_len = 0
        s1_char_usages = defaultdict(int)
        for char in s1:
            s1_char_usages[char] += 1
            s1_len += 1

        cur_sub_str = defaultdict(int)

        l = 0
        for r in range(len(s2)):
            if (r - l + 1) > s1_len:
                cur_sub_str[s2[l]] -= 1
                if cur_sub_str[s2[l]] == 0:
                    cur_sub_str.pop(s2[l])
                l += 1

            cur_sub_str[s2[r]] += 1
            if s1_char_usages == cur_sub_str:
                return True

        return False


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

    def test_has_perm(self):
        self.e(args=dict(s1="abc", s2="lecabee"), expected=True)

    def test_no_perm(self):
        self.e(args=dict(s1="abc", s2="lecaabee"), expected=False)


if __name__ == "__main__":
    unittest.main()
# brute force
# def run(self, s1: str, s2: str) -> bool:
#     s1_len = 0
#     s1_char_usages = defaultdict(int)
#     for char in s1:
#         s1_char_usages[char] += 1
#         s1_len += 1

#     cur_sub_str = defaultdict(int)

#     l = 0
#     for r in range(len(s2)):
#         if (r - l + 1) > s1_len:
#             cur_sub_str[s2[l]] -= 1
#             if cur_sub_str[s2[l]] == 0:
#                 cur_sub_str.pop(s2[l])
#             l += 1

#             cur_sub_str[s2[r]] += 1
#             if s1_char_usages == cur_sub_str:
#                 return True

#         return False

# optimal
# compares number of matching char counts in linear time
#
# iterates through both at once to
# def checkInclusion(self, s1: str, s2: str) -> bool:
#     if len(s1) > len(s2):
#         return False

#     s1Count, s2Count = [0] * 26, [0] * 26
#     for i in range(len(s1)):
#         s1Count[ord(s1[i]) - ord("a")] += 1
#         s2Count[ord(s2[i]) - ord("a")] += 1

#     matches = 0
#     for i in range(26):
#         matches += 1 if s1Count[i] == s2Count[i] else 0

#     l = 0
#     for r in range(len(s1), len(s2)):
#         if matches == 26:
#             return True

#         index = ord(s2[r]) - ord("a")
#         s2Count[index] += 1
#         if s1Count[index] == s2Count[index]:
#             matches += 1
#         elif s1Count[index] + 1 == s2Count[index]:
#             matches -= 1

#         index = ord(s2[l]) - ord("a")
#         s2Count[index] -= 1
#         if s1Count[index] == s2Count[index]:
#             matches += 1
#         elif s1Count[index] - 1 == s2Count[index]:
#             matches -= 1
#         l += 1
#     return matches == 26
