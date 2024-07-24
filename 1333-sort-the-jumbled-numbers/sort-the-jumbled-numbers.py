class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [num for _, num in sorted(enumerate(nums), key=lambda x: (int(''.join(str(mapping[int(digit)]) for digit in str(x[1]))), x[0]))]