class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        for i in range(len(nums)):
            if i > maxjump:
                return False
            if maxjump >= len(nums)-1:
                return True
            maxjump = max(maxjump,i+nums[i])
            print(maxjump)
        return False