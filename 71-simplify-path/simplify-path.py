class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        res=path.split('/')
        for s in res:
            if s=="":
                continue
            if s==".":
                continue
            elif s=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        if stack:
            return '/'+'/'.join(stack)
        else:
            return '/'