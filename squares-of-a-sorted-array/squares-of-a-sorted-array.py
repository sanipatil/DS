class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, k, j = 0,len(nums)-1, len(nums)-1
        result = [None] * len(nums)
        while k >= 0:
            if abs(nums[i]) > abs(nums[j]):
                square = nums[i] ** 2
                i += 1
            else:
                square = nums[j] ** 2
                j -= 1
            result[k] = square
            k -= 1
        return result