class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        nums = [0] * len(target)     
        for i,j,k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                nums[0] = max(nums[0],i)            
                nums[1] = max(nums[1],j)
                nums[2] = max(nums[2],k)
                if nums == target:
                    return True            
        return False