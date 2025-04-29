class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
          max_ele = max(nums)
          n = len(nums)
          ans = 0 
          cnt = 0 
          left = 0 
          for right in range(n):
            if nums[right] == max_ele: 
               cnt += 1 
            
            while cnt >= k:
                ans += n - right  
                if nums[left] == max_ele:
                    cnt -= 1
                left += 1
          
          return ans 