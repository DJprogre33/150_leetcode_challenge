class Solution:
    """link to the problem: https://leetcode.com/problems/product-of-array-except-self/"""
    @staticmethod
    def v1_product_except_self(nums: list[int]) -> list[int]:
        """
        Time complexity: O(n) 201ms beats 79.21%
        Space complexity: 0(n) 25.40mb beats 20.32 %
        """
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # fill prefix
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        # fill postfix
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        # compute result
        result = [prefix[i] * postfix[i] for i in range(len(nums))]
        return result

    @staticmethod
    def v2_product_except_self(nums: list[int]) -> list[int]:
        """
        Time complexity: O(n) 199ms beats 81.05%
        Space complexity: 0(1) except result, 23.74mb beats 75.22 %
        """
        result = [1] * len(nums)

        # first iteration (computing prefix)
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        # compute result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix *= nums[i]
        return result


print(Solution.v2_product_except_self([1,2,3,4]))