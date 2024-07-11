class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for char in s:
            if char==")":
                temp=""
                while stack:
                    ch=stack.pop()
                    if ch=="(":
                        break
                    temp+=ch
                for char in temp:
                    stack.append(char)
                
            else:
                stack.append(char)
        return "".join(stack)

        # ed et co el
        # ed octe el
        # leetcode