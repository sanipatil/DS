class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["/","*","+","-"]
        for i in range(len(tokens)):
            if tokens[i] in operations:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if tokens[i] == '/':
                    result = int(operand2 / operand1)
                elif tokens[i] == '*':
                    result = operand2 * operand1
                elif tokens[i] == '+':
                    result = operand2 + operand1
                elif tokens[i] == '-':
                    result = operand2 - operand1
                stack.append(result)
            else:
                stack.append(tokens[i])
        return stack.pop()