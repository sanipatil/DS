class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)>1):
            j = 0
            i = 1
            while i<len(nums):
                if nums[i] != nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j+1]
                    nums[j+1] = temp
                    j+=1
                i+=1
            return j+1