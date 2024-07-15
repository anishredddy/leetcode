class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 < p2:
            current_sum = numbers[p1] + numbers[p2]
            if current_sum == target:
                return [p1 + 1, p2 + 1]
            elif current_sum < target:
                p1 += 1
            else:
                p2 -= 1
        