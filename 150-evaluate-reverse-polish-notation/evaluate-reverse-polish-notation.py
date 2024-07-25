class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                if token == '+':
                    result = a1 + a2
                elif token == '-':
                    result = a1 - a2
                elif token == '*':
                    result = a1 * a2
                else:
                    result = int(a1 / a2)
                stack.append(result)
        return stack.pop()