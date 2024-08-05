class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct=set()
        duplicate=set()

        for s in arr:
            if s in duplicate:
                continue
            if s in distinct:
                distinct.remove(s)
                duplicate.add(s)
            else:
                distinct.add(s)
        for s in arr:
            if s not in duplicate:
                k-=1
            if k==0:
                return s
        return ""        