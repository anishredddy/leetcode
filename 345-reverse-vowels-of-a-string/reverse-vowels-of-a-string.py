class Solution:
    def reverseVowels(self, s: str) -> str:
        q=deque()
        a={'a','A','e','E','i','I','o','O','u','U'}
        for i in range(len(s)):
            if s[i] in a:
                q.append((s[i],i))
        s=list(s)
        while len(q)>=2:
            left,right=q.popleft(),q.pop()
            s[left[1]]=right[0]
            s[right[1]]=left[0]
        return ''.join(s)