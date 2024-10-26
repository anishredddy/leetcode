class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operation=[]
        stack=[]

        for char in expression:
            if char=="&" or char=="!" or char=="|":
                operation.append(char)
            elif char==")":
                # print(stack)
                # print("op",operation)
                #todo pop operation
                sign=operation.pop()
                if sign=="!":
                    ch=stack.pop()
                    stack.pop()
                    stack.append(not ch)
                elif sign=="|":
                    char=stack.pop()
                    res=False
                    while char!="(":
                        res=res|char
                        char=stack.pop()
                    stack.append(res)
                elif sign=="&":
                    char=stack.pop()
                    res=True
                    while char!="(":
                        res=res&char
                        char=stack.pop()
                    stack.append(res)
            else:
                if char=="t":
                    stack.append(True)
                elif char=="f":
                    stack.append(False)
                elif char=="(":
                    stack.append(char)
                    #(
        return stack.pop()