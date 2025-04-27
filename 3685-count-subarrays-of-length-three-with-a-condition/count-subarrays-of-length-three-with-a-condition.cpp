class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int size = nums.size();
        int count = 0;

        // Iterate through the array, ensuring there are at least 3 elements
        for (int i = 1; i < size - 1; ++i) {
            // Check if the sum of the first and third elements equals half of the second element and 
            // check only if the num[i] divisible by 2 
            if (nums[i] % 2 == 0 && (nums[i - 1] + nums[i + 1]) == nums[i] / 2) {
                count++;
            }
        }

        return count; //sornam.t 
    }
};