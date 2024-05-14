class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0

        # number of elements on the right side < value of element
        # 0 1 3 5 6

        