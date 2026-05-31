class Solution:
    def maxArea(self, h: List[int]) -> int:
        
        maxi = 0
        left = 0
        right = len(h)-1
        while(left<right):
            expected = (right-left)*min(h[right],h[left])
            maxi = expected if expected>maxi else maxi
            if h[left] > h[right]:
                right -= 1
            else:
                left += 1
        
        return maxi
            