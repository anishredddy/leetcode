class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(pair,score):
            nonlocal s
            res=0
            stack=[]
            for char in s:
                if char==pair[1] and stack and stack[-1]==pair[0]:
                    res+=score
                    stack.pop()
                else:
                    stack.append(char)
            s="".join(stack)
            print(res)
            return res
        res=0
        if x>=y:
            res+=remove("ab",x)
            res+=remove("ba",y)
        else:
            res+=remove("ba",y)
            res+=remove("ab",x)
        return res