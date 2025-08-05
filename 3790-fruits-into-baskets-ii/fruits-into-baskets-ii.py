class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res=0
        for f in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j]>=fruits[f]:
                    baskets[j]=-1
                    fruits[f]=-1
                    break
            if fruits[f]!=-1:
                res+=1
        return res