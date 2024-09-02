class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits=="":
            return []
        def dfs(i,currStr):
            if i==len(digits):
                res.append(currStr)
                return
            for char in digitToChar[digits[i]]:
                dfs(i+1,currStr+char)
        dfs(0,"")
        return res