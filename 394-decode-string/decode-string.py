class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res=""
        for char in s:
            if char=="]":
                #todo
                s=""
                while stack and stack[-1]!="[":
                    s=stack.pop()+s
                stack.pop()
                count=""
                while stack and stack[-1].isdigit():
                    count=stack.pop()+count
                count=int(count)
                stack.append(s*count)
            else:
                stack.append(char)
        return ''.join(stack)