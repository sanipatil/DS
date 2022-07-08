class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapDict = {
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        result = []
        combination = ""
        def dfs(i,combination):
            if len(digits) <= 0:
                return
            if len(combination) == len(digits):
                result.append(combination)
                return 
            for ch in mapDict[digits[i]]:
                dfs(i+1,combination+ch)
        
        dfs(0,combination)
        return result
        
        
        