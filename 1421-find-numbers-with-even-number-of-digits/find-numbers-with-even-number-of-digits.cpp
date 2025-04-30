class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int result = 0; 
        for (int num:nums){
            int dig_num = 0 ; 
            while(num){
                num/= 10;
                dig_num++;
            }
            if(dig_num%2==0)
            {
                result++;
            }
        }
        return result;
    }
};