class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        
        def dfs(start, path):
            if start == len(s):
                res.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    dfs(end, path + [s[start:end]])
        
        dfs(0, [])
        return res
