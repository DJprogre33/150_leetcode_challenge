class Solution:
    """link to the problem: https://leetcode.com/problems/group-anagrams/"""
    @staticmethod
    def v1_top_k_frequent(nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n*logn) 95ms beats 92.53%
        Space complexity: 0(n) 21.06mb beats 70.93%
        """
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        return sorted(hashmap, key=lambda x: -hashmap[x])[:k]

    @staticmethod
    def v2_top_k_frequent(nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n) 109ms beats 67.89%
        Space complexity: 0(n) 22.08mb beats 10.12%
        """
        # using bucket sort
        hashmap = {}
        # initialize the list of frequents (index = total n count)
        freq = [[] for i in range(len(nums) + 1)]
        # count numbers
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        # update freq
        for n, c in hashmap.items():
            freq[c].append(n)

        res = []
        start_idx = len(freq) - 1
        while k:
            # iterate through freq and add values in result
            for number in freq[start_idx]:
                res.append(number)
                k -= 1
            start_idx -= 1
        return res


print(Solution.v2_top_k_frequent([1], 1))

