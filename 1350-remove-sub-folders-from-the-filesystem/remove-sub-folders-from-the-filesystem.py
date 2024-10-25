class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        hashSet=set(folder)
        res=[]
        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i]=="/" and f[:i] in hashSet:
                    res.pop()
                    break
        return res
