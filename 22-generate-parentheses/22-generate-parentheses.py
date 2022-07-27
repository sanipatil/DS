class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(curr, stack):
            if len(curr) == 2 * n:
                # print(curr, stack)
                if not stack:
                    result.append(curr)
                return
            
            stack.append('(')
            dfs(curr + '(', stack)
            stack.pop()
            
            t = ''
            if stack:
                t = stack.pop()
            if t == '(':
                dfs(curr + ')', stack)
                stack.append(t)
            
        dfs('(',['('])
        return result
                