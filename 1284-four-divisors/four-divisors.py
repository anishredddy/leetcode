class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            count = 0
            total = 0
            i = 1

            while i * i <= num:
                if num % i == 0:
                    d1 = i
                    d2 = num // i

                    if d1 == d2:
                        count += 1
                        total += d1
                    else:
                        count += 2
                        total += d1 + d2

                    if count > 4:
                        break
                i += 1

            if count == 4:
                ans += total

        return ans
