class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        combination = []
        def dfs(i,combination,currentSum):
            if currentSum == target:
                result.append(combination.copy())
                return 
            if i > len(candidates)-1 or currentSum > target:
                return
            combination.append(candidates[i])
            dfs(i+1,combination,currentSum + candidates[i])
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            combination.pop()
            dfs(i+1,combination,currentSum)
            
        dfs(0,combination,0)
        return result