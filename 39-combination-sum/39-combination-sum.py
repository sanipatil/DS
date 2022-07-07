class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        def dfs(i,combination,currentSum):
            if currentSum == target:
                result.append(combination.copy())
                return 
            if i > len(candidates)-1 or currentSum > target:
                return
            combination.append(candidates[i])
            dfs(i,combination,currentSum+candidates[i])
            combination.pop()
            dfs(i+1,combination,currentSum)
            
        dfs(0,combination,0)
        return result