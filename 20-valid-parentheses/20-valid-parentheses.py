class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = False
        for i in range(len(s)):
            if s[i] =='(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if stack:
                    ele = stack.pop()
                    if ele == '(' and s[i] == ')':
                        flag=True
                    elif ele == '[' and s[i] == ']':
                        flag=True
                    elif ele == '{' and s[i] == '}':
                        flag =True
                    else:
                        return False
                else:
                    return False
            
        if stack:
            return False
        else:
            return flag