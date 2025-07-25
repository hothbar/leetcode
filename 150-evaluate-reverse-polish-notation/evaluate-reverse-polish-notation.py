class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack
        # If the token is a digit, add to the stack
        # If taken is an operator, pop from the stack and multiply numbers on top

        stack = []
        
        for t in tokens:

            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)

            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                
            else:
                stack.append(int(t))
        
        return stack[0]
                
        