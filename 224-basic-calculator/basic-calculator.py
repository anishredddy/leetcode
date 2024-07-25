class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)

        stack = []
        num = 0
        sign = "+"
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-()" or i == len(s) - 1:
                if s[i] == '(':
                    j = i + 1
                    bal = 1
                    while j < len(s):
                        if s[j] == '(':
                            bal += 1
                        if s[j] == ')':
                            bal -= 1
                        if bal == 0:
                            break
                        j += 1
                    num = self.calculate(s[i+1:j])
                    i = j
                update(sign, num)
                num = 0
                sign = s[i]
            i += 1
        
        update(sign, num)
        return sum(stack)