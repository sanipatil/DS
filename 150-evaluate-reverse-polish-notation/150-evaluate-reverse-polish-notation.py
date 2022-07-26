class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i=0
        while len(tokens) != 1:
            if tokens[i] == '/':
                tokens[i-2] = int(int(tokens[i-2]) / int(tokens[i-1]))
                del tokens[i-1:i+1]
                i = i-2
            elif tokens[i] == '*':
                tokens[i-2] = int(tokens[i-2]) * int(tokens[i-1])
                del tokens[i-1:i+1]
                i = i-2
            elif tokens[i] == "+":
                tokens[i-2] = int(tokens[i-2]) + int(tokens[i-1])
                del tokens[i-1:i+1]
                i = i-2
            elif tokens[i] == '-':
                tokens[i-2] = int(tokens[i-2]) - int(tokens[i-1])
                del tokens[i-1:i+1]
                i = i-2
            i += 1
            if i >= len(tokens):
                i=0
                
        return tokens[0]