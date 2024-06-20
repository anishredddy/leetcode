class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #one ball will always be at first
        # one ball will always be at last
        # we need to place n-2 balls in (1,n) whatever basket is available


        #brute force try every combination - does not work - n*n
        # sorted - binary search ?

        #do binary search and then find closest number to mid?



        position.sort()
        low=0
        high=position[-1]-position[0]


        def valid(x):
            prev=position[0]
            count=1
            for p in position:
                if p-prev>=x:
                    count+=1
                    prev=p
                if count==m:
                    return True
            return False
        print(position)
        while low<=high:
            mid=(low+high)//2
            if valid(mid):
                low=mid+1
            else:
                high=mid-1
        return high