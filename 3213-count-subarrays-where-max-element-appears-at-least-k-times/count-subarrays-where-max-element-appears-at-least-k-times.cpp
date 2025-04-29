class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int max_num = *max_element(nums.begin(), nums.end());
        long long ans = 0 ; 
        int count = 0; 
        int left = 0; 

        for (int right = 0; right<n; right++){
            if (nums[right] == max_num){
                count++;
            }
            while(count >= k){
                ans += (n-right);
                if (nums[left] == max_num){
                    count--;
                }
                left++;
            }
        }
        return ans; //sornam.t
        
    }
};