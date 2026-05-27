class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        r = len(n) - 1
        l = 0

        while(l<r):
            current_sum = n[l]+n[r]

            if current_sum == target:
                return [l+1,r+1]
            
            elif current_sum > target:
                r -=1
            else:
                l +=1
