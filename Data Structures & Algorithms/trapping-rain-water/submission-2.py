class Solution:
    def trap(self, h: List[int]) -> int:
        
        left = 0
        right = len(h)-1
        lmax = 0
        rmax = 0
        total = 0
        while(left<right):
            lmax = max(lmax,h[left])
            rmax = max(rmax,h[right])
            if lmax>rmax:
                total += rmax - h[right]
                right -=1
            else:
                total += lmax - h[left]
                left += 1
        print(f"Total = {total}\nL: {lmax}\nR: {rmax}")
        return total
        
