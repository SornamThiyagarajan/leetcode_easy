class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        long long n = nums.size();
        long long left = 0, right = 0; 
        long long sum = 0, count = 0; 
        
        while(left < n ){
            //Find the larget valid window 
            while (right < n and (sum+nums[right])*(right-left+1)<k)
                sum += nums[right++];
            count += right-left; 

            //slide the window forward by removing nums[left]
            if (right == left)
                right++;
            else
                sum -= nums[left];
            
            left++;
        }
        return count;
        
    }
};