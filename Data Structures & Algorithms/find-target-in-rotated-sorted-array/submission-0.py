class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search on the array with note on the inflection point since array is rotated right and is circular.
        

        """
        def binary_search(left: int, right: int):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            return -1

        # Find the pivot then perform binary search on both subarrays (left-pivot and pivot-end).
        # Pivot can be found by binary search expansion from the left since its an ascending order array
        # no matter where the pivot is at.
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        pivot = l

        res = binary_search(0, pivot - 1)
        if res != -1: return res
        return binary_search(pivot, len(nums) - 1)