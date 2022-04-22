class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j = 0, 0
        while i <= len(nums)-1:
            if nums[i] % 2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
            i += 1
        return nums