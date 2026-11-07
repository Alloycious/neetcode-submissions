class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Since tokens represent a valid arithmetic expression in postfix reverse polish notation,
        we can use a stack to solve. If a token is a number, apped to the stack, else if
        token is in the set of valid operators (+, -, *, /), pop the last two tokens / numbers
        and operate them.
        """
        if len(tokens) == 1: return int(tokens[0])

        stack = []
        operators = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
            "*": lambda a,b: a * b, 
            "/": lambda a, b: int(a / b)
        }
        for token in tokens:
            if token in operators:
                # Perform operation on left operand with right operand.
                # Since we're using a stack and popping of it, we must switch the
                # order of the operands when performing the operation.
                operand_1, operand_2 = stack.pop(), stack.pop()
                res = operators[token](int(operand_2), int(operand_1))
                stack.append(res)
            else:
                # Since only numbers and operation tokens are in tokens List
                # we assume the rest are numbers, whether positive or negative.
                stack.append(int(token))

        # Last result is left in the stack.
        return int(stack[-1])
