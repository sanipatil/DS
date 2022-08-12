class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        dp[n-1] = 0
        for i in range(n-2,-1,-1):
            if nums[i] != 0:
                dp[i] = min(dp[i+1:i+nums[i]+1]) + 1
        
        return dp[0]