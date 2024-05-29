class Solution:
    def numSteps(self, s: str) -> int:
        res = 0

        def steps(s):
            nonlocal res
            print(res, s) 
            if s == '1':
                return
            if s[-1] == '1':
                i = len(s) - 1
                while i > 0 and s[i] == '1':
                    i -= 1
                if i == 0:
                    s = '1' + '0' * len(s) 
                else:
                    s = s[:i] + '1' + '0' * (len(s) - i - 1)
                res += 1
                steps(s)
            elif s[-1] == '0':
                res += 1
                steps(s[:-1])

        steps(s)
        return res
