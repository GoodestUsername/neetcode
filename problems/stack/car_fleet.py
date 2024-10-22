from collections import defaultdict
from math import ceil, inf
from typing import List
import unittest
import sys

sys.tracebacklimit = 0

# rules
# car cannot pass a car in front of it, it slows down to the car in front's speed

# part of the fleet if:
# * same speed and same position
# * at destination at the same time
# * just by itself

# observations
# * car with slower speed and behind will not become a fleet with a faster card UNLESS
# *** it's at the target at the same time
# * car with faster speed and behind will is part of the fleet with min speed of fleet

# * car since car can only catch up, any car that catches up to another is part of the fleet
# * the front of the positions at lowest speed will cause all the others to be part of it given enough time to distance

# strats
# * check every car from far to left for lowest speeds
# *** every card behind and has faster speed that "will reach the target" before it theoretically
# *** is part of the same fleet


class Solution:
    def run(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets_stack = []

        for car in cars:
            time_to_target = (target - car[0]) / car[1]

            if len(fleets_stack) > 0 and fleets_stack[-1] >= time_to_target:
                continue
            else:
                fleets_stack.append(time_to_target)

        return len(fleets_stack)


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

    def test_big_target(self):
        self.e(
            args=dict(target=100, position=[0, 2, 4], speed=[4, 2, 1]),
            expected=1,
        )

    def test_dup(self):
        self.e(args=dict(target=10, position=[1, 4], speed=[3, 2]), expected=1)

    def test_fleet_both_end(self):
        self.e(
            args=dict(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]),
            expected=3,
        )

    def test_fleet_first_last(self):
        self.e(
            args=dict(target=10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]), expected=3
        )


if __name__ == "__main__":
    unittest.main()
