class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Minima L, and maxima R pointer
        i, j = 0, len(numbers) - 1

        while i < j:
            res = numbers[i] + numbers[j]
            if res > target:
                j -= 1
            elif res < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return []
