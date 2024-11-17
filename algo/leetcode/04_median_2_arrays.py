# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Difficulty: Hard
# 03.03.2024

from typing import List


class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3: List[int] = []
        i, j = 0, 0
        for _ in range(len(nums1) + len(nums2)):
            if i == len(nums1):
                nums3.append(nums2[j])
                j += 1
            elif j == len(nums2):
                nums3.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        return nums3

    def median(self, nums: List[int]) -> float:
        mid = len(nums) / 2
        if mid.is_integer():
            return (nums[int(mid - 1)] + nums[int(mid)]) / 2
        else:
            return nums[int(mid)]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force
        # nums3: List[int] = nums1 + nums2
        # sorted_nums3 = sorted(nums3)
        # mid = len(sorted_nums3) / 2
        # if mid.is_integer():
        #     return (sorted_nums3[int(mid-1)] + sorted_nums3[int(mid)]) / 2
        # else:
        #     return sorted_nums3[int(mid)]

        # Binary Search
        # Edge cases
        if len(nums1) == 0:
            return self.median(nums2)
        if len(nums2) == 0:
            return self.median(nums1)


def main():
    try:
        assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
        assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
        assert Solution().findMedianSortedArrays([0, 0], [0, 0]) == 0.0
        assert Solution().findMedianSortedArrays([], [1]) == 1.0
        assert Solution().findMedianSortedArrays([], [2, 3]) == 2.5
        assert Solution().findMedianSortedArrays([2], []) == 2.0
        assert Solution().findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]) == 3.5
        print("Passed all test cases!")
    except AssertionError:
        print("Failed test cases! Please, debug!")


if __name__ == "__main__":
    main()
