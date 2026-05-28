class Solution:
    def threeSum(self, l: List[int]) -> List[List[int]]:
        #sorting (insertion)
        for i in range(1,len(l)):
            j = i
            while j>0 and l[j-1] > l[j]:
                l[j-1],l[j]=l[j],l[j-1]
                j-=1
        
        ls = []
        #main_loop
        for i in range(len(l)):

            if l[i]>0:
                break
            if i>0 and l[i] == l[i-1]:
                continue
            
            right = len(l)-1
            left = i+1
            while(left<right):
                if l[i]+l[left]+l[right] == 0:
                    ls.append([l[i],l[left],l[right]])
                    left += 1
                    while left < right and l[left] == l[left - 1]:
                        left += 1
                elif l[i]+l[left]+l[right] > 0:
                    right -= 1
                else:
                    left +=1    
            
        return ls
                

        

       