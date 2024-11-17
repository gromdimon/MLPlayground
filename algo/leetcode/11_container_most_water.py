# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# 10.03.2024

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_pos = 0
        end_pos = len(height) - 1
        max_vol = 0
        while end_pos - start_pos >= 1:
            start_h = height[start_pos]
            end_h = height[end_pos]
            vol = (end_pos - start_pos) * min(start_h, end_h)
            if vol > max_vol:
                max_vol = vol
            if start_h <= end_h:
                curr_h = start_h
                while curr_h <= start_h and start_pos < end_pos:
                    start_pos += 1
                    curr_h = height[start_pos]
            else:
                curr_h = end_h
                while curr_h <= end_h and start_pos < end_pos:
                    end_pos -= 1
                    curr_h = height[end_pos]
        return max_vol

        # # Find possible start_positions
        # start_positions = []
        # max_start = 0
        # for start_id, start_height in enumerate(height):
        #     if start_height > max_start:
        #         start_positions.append(start_id)
        #         max_start = start_height

        # end_positions = []
        # max_end = 0
        # height_len = len(height)
        # # Find possible end_positions
        # for end_id, end_height in enumerate(height[::-1]):
        #     if end_height > max_end:
        #         end_positions.append(height_len - end_id - 1)
        #         max_end = end_height

        # max_vol = 0
        # for start in start_positions[::-1]:
        #     for end in end_positions:
        #         if end <= start:
        #             break
        #         vol = (end - start) * min(height[start], height[end])
        #         if vol > max_vol:
        #             max_vol = vol
        # return max_vol

        # Brute Forcee
        # if len(height) < 2:
        #     return 0
        # max_vol = 0
        # for start_id, start_height in enumerate(height):
        #     for end_id, end_height in enumerate(height[start_id:]):
        #         # Actual End position is start_id + end_id
        #         volume = end_id * min(start_height, end_height)
        #         if volume > max_vol:
        #             max_vol = volume

        # return max_vol


def main():
    try:
        assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert Solution().maxArea([1, 1]) == 1
        assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
        assert Solution().maxArea([1, 2, 1]) == 2
        print("Passed all test cases!")
    except AssertionError:
        print("Failed test cases! Please, debug!")


if __name__ == "__main__":
    main()
