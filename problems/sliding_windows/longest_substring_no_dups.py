from collections import defaultdict
from typing import List
import unittest


class Solution:
    def run(self, s: str) -> int:
        max_substr = 0
        curr_len = 0
        start_index = 0
        used = defaultdict(bool)

        for char in s:
            max_substr = max(max_substr, curr_len)

            while char in used:
                used.pop(s[start_index])
                start_index += 1
                curr_len -= 1
            else:
                curr_len += 1
                used[char] = True

        return max(max_substr, curr_len)


class tests(unittest.TestCase):
    # region setup/teardown
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        self.solution = None

    # endregion setup/teardown

    def e(self, args, expected):
        answer = self.solution.run(args)
        self.assertEqual(answer, expected)

    # def test_long(self):
    #     self.e(args="zxyzxyz", expected=3)

    # def test_single(self):
    #     self.e(args="xxxxx", expected=1)

    def test_middle(self):
        self.e(args="pwwkew", expected=3)


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
