from collections import defaultdict
from typing import Any, List, Tuple


def b_search(nums: List[Tuple[float, Any]], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m][0] > target:
            r = m - 1
        elif nums[m][0] < target:
            l = m + 1
        else:
            return m
    return l - 1


class TimeMap:
    def __init__(self):
        self._map = defaultdict(list)
        self._time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        location = b_search(self._map[key], timestamp)
        if location == -1:
            if len(self._map[key]) and timestamp >= self._map[key][-1][0]:
                return self._map[key][-1][1]
            return ""

        print(self._map[key], location)
        return self._map[key][location][1]


case_1 = [
    "TimeMap",
    "set",
    ["alice", "happy", 1],
    "get",
    ["alice", 1],
    "get",
    ["alice", 2],
    "set",
    ["alice", "sad", 3],
    "get",
    ["alice", 3],
]

case_2 = [
    "TimeMap",
    "set",
    ["test", "one", 10],
    "set",
    ["test", "two", 20],
    "set",
    ["test", "three", 30],
    "get",
    ["test", 15],
    "get",
    ["test", 25],
    "get",
    ["test", 35],
]

Input = [
    "TimeMap",
    "set",
    ["alice", "happy", 1],
    "get",
    ["alice", 1],
    "get",
    ["alice", 2],
    "set",
    ["alice", "sad", 3],
    "get",
    ["alice", 3],
]

Output = [None, None, "happy", "happy", None, "sad"]

# Explanation =
time_map = TimeMap()
time_map.set("alice", "happy", 1)
# store the key "alice" and value "happy" along with timestamp = 1.
time_map.get("alice", 1)
# return "happy"
time_map.get("alice", 2)
# return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
time_map.set("alice", "sad", 3)
# store the key "alice" and value "sad" along with timestamp = 3.
time_map.get("alice", 3)
# return "sad"

# other solution
# class TimeMap:
#     def __init__(self):
#         self.keyStore = {}  # key : list of [val, timestamp]

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.keyStore:
#             self.keyStore[key] = []
#         self.keyStore[key].append([value, timestamp])

#     def get(self, key: str, timestamp: int) -> str:
#         res, values = "", self.keyStore.get(key, [])
#         l, r = 0, len(values) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if values[m][1] <= timestamp:
#                 res = values[m][0]
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res
