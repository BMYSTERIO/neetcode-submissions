from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        track = {}
        track_len = []
        ind_track = 0

        for i in range(len(nums)):
            num = nums[i]

            
            if num - 1 not in nums:
                track[ind_track] = [num]
                
                curr = num
                while curr + 1 in nums:
                    track[ind_track].append(curr + 1)
                    curr += 1
                    
                ind_track += 1

       
        for l in track.values():
            track_len.append(len(l))
        
        
        return max(track_len) if track_len else 0