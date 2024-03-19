class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        # reached bottom
        if len(nums) == 1:
            new_perm = [nums.copy()]
            return new_perm
        
        for idx in range(len(nums)):
            # take out one item from the list, that cannot be in child nodes
            num = nums.pop(0)

            # recursive branch
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(num)
            permutations.extend(perms)
            
            # cleanup
            nums.append(num)

        return permutations