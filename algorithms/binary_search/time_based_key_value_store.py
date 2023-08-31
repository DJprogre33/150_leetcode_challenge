class TimeMap:
    """link to the problem: https://leetcode.com/problems/time-based-key-value-store/"""

    # Time complexity: O(logN) 715ms beats 49.20%
    # Space complexity: 0(n) 73.88mb beats 80.42%

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.hashmap.get(key)
        if values:
            left, right = 0, len(values) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if values[mid][-1] == timestamp:
                    result = values[mid][0]
                    break

                if values[mid][-1] < timestamp:
                    result = values[mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
        return result


