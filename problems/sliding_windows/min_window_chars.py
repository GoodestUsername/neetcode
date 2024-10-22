from calendar import c
from collections import defaultdict
from math import inf
from re import L
from typing import List
import unittest
import sys

sys.tracebacklimit = 0


class Solution:
    def run(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = {}

        if len(t) > len(s):
            return ""

        matched = defaultdict(bool)
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
            matched[t[i]] = False

        location_map: dict[str, List[int]] = {}
        for i in range(len(s)):
            curr_list = location_map.get(s[i], [])
            curr_list.append(i)
            location_map[s[i]] = curr_list

        if s == t:
            return t

        cur_substr = ""
        min_substr_len = inf

        l = 0
        required_matches = len(t_map)

        for r in range(len(s)):
            if t_map.get(s[r], 0) == 0 and len(t_map) == required_matches:
                l += 1

            if (
                s_map[s[r]] == t_map.get(s[r], -1)
                and len(t_map) - 1 == required_matches
                and r > 0
                and s[r] == s[r - 1]
            ):
                l += 1

            if min_substr_len != int and (r - l + 1) >= min_substr_len:
                l = r - min_substr_len + 1

            if t_map.get(s[r], 0) > s_map[s[r]]:
                s_map[s[r]] += 1

            if s_map[s[r]] == t_map.get(s[r], -1) and t_map.get(s[r], 0) > 0:
                if required_matches > 0 and not matched.get(s[r], False):
                    matched[s[r]] = True
                    required_matches -= 1

            if required_matches == 0:
                cur_len = min(min_substr_len, r - l + 1)
                if min_substr_len > cur_len:
                    min_substr_len = cur_len
                    cur_substr = s[l : r + 1]

                s_map[s[l]] -= 1
                matched[s[l]] = False
                l += 1
                required_matches += 1

                while len(s) > l and t_map.get(s[l], 0) == 0:
                    if s_map[s[l]] > 0:
                        s_map[s[l]] -= 1
                    matched[s[l]] = False
                    l += 1

        return cur_substr


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

    def test_second_substr_inaccessible_to_first(self):
        self.e(args=dict(s="ADOBECODEBANC", t="ABC"), expected="BANC")

    def test_two(self):
        self.e(args=dict(s="OUZODYXAZV", t="XYZ"), expected="YXAZ")

    def test_equal(self):
        self.e(args=dict(s="xyz", t="xyz"), expected="xyz")

    def test_single(self):
        self.e(args=dict(s="a", t="a"), expected="a")

    def test_min_non_identical(self):
        self.e(args=dict(s="ab", t="a"), expected="a")

    def test_high_repetition(self):
        self.e(args=dict(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"), expected="abbbbbcdd")

    def test_empty(self):
        self.e(args=dict(s="x", t="xy"), expected="")


if __name__ == "__main__":
    unittest.main()

# more concise solution
# def run(self, s: str, t: str) -> str:
#     if t == "":
#         return ""

#     countT, window = {}, {}
#     for c in t:
#         countT[c] = 1 + countT.get(c, 0)

#     have, need = 0, len(countT)
#     res, resLen = [-1, -1], float("infinity")
#     l = 0
#     for r in range(len(s)):
#         c = s[r]
#         window[c] = 1 + window.get(c, 0)

#         if c in countT and window[c] == countT[c]:
#             have += 1

#         while have == need:
#             if (r - l + 1) < resLen:
#                 res = [l, r]
#                 resLen = r - l + 1

#             window[s[l]] -= 1
#             if s[l] in countT and window[s[l]] < countT[s[l]]:
#                 have -= 1
#             l += 1
#     l, r = res
#     return s[l : r + 1] if resLen != float("infinity") else ""
