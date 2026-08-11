class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()
        result = None
        operators = ["+", "*", "-", "/"]

        # Assuming the input is always valid
        for token in tokens:
            if token not in operators:
                dq.append(int(token)) # Put them as numbers
                continue
            
            secondNum = dq.pop()
            firstNum = dq.pop()

            if token == "+":
                result = firstNum + secondNum                
            elif token == "-":
                result = firstNum - secondNum                
            elif token == "*":
                result = firstNum * secondNum
            elif token == "/":
                result = int(firstNum / secondNum) # Rounding to 0
            
            dq.append(result)
            
        # Final result is in the deque
        return dq[-1]
        

