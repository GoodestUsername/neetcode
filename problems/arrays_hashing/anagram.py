from math import floor
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for s_char, t_char in zip(s, t):
            if s_char in sDict:
                sDict[s_char] += 1
            else:
                sDict[s_char] = 1
            if t_char in tDict:
                tDict[t_char] += 1
            else:
                tDict[t_char] = 1

        return sDict == tDict


class tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def e(self, args, expected):
        answer = self.solution.run(**args)
        self.assertEqual(answer, expected)

    def tearDown(self):
        self.solution = None

    def test_anagram(self):
        self.e(args=dict(s="racecar", t="carrace"), expected=True)

    def test_n_anagram(self):
        self.e(args=dict(s="jar", t="jam"), expected=False)


if __name__ == "__main__":
    unittest.main()


# optimal
# s loop: subtracts for each instance of char
# t loop: adds for each instance of char
# sum should be 0 if they are anagrams
# class Solution:
#     def run(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = [0] * 26
#         for i in range(len(s)):
#             count[ord(s[i]) - ord("a")] += 1
#             count[ord(t[i]) - ord("a")] -= 1

#         for val in count:
#             if val != 0:
#                 return False
#         return True
