class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        palindrome = []
        def isPalindrome(s,i,j):
            while i<j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        def dfs(i):
            if i >= len(s):
                result.append(palindrome.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s,i,j):
                    palindrome.append(s[i:j+1])
                    dfs(j+1)
                    palindrome.pop()
        
        dfs(0)
        return result