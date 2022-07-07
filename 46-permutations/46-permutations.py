class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = []
        def dfs(permutations):
            if len(permutations) == len(nums):
                result.append(permutations.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in permutations:
                    permutations.append(nums[i])
                    dfs(permutations)
                    permutations.pop()
        
        dfs(permutations)
        return result