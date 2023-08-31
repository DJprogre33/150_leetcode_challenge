class Solution:
    """link to the problem: https://leetcode.com/problems/median-of-two-sorted-arrays/"""
    @staticmethod
    def v1_find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
        """
        Time complexity: O(log(m+n) ms beats %
        Space complexity: 0(1) mb beats %
        """

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        left_1, right_1 = 0, len(nums1) - 1
        while True:
            mid_1 = left_1 + (right_1 - left_1) // 2
            remain_2 = half - mid_1 - 2

            n1_left = nums1[mid_1] if mid_1 >= 0 else float("-infinity")
            n1_right = nums1[mid_1 + 1] if (mid_1 + 1) >= len(nums1) else float("infinity")
            n2_left = nums2[remain_2] if remain_2 >= 0 else float("-infinity")
            n2_right = nums2[remain_2 + 1] if (remain_2 + 1) < len(nums2) else float("infinity")

            if n1_left <= n2_right and n2_left <= n1_right:
                if total % 2:
                    return min(n1_right, n2_right)
                else:
                    return (max(n1_left, n2_left) + min(n1_right, n2_right)) / 2
            elif n1_left > n2_right:
                right_1 = mid_1 - 1
            else:
                left_1 = mid_1 + 1
