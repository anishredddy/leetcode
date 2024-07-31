class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        mem={}
        def helper(i):
            if i==len(books):
                return 0
            if i in mem:
                return mem[i]
            
            width=shelfWidth
            max_h=0
            mem[i]=float('inf')

            for j in range(i,len(books)):
                curr_w,curr_h=books[j]
                if curr_w>width:
                    break
                
                width-=curr_w
                max_h=max(max_h,curr_h)
                mem[i]=min(mem[i],helper(j+1)+max_h)
            return mem[i]
        return helper(0)