class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sort array to enable two pointers approach
        numbers.sort()

        # Minima L pointer
        i = 0

        # Maxima R pointer
        j = len(numbers) - 1

        # Results
        res = 0

        while i < j:
            res = numbers[i] + numbers[j]
            if res > target:
                j -= 1
            elif res < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return []
