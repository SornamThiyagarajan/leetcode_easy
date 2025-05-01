class Solution {
public:
    bool isPalindrome(int x) {
         // Negative numbers are not palindrome
        // Numbers ending in 0 (but not 0 itself) are also not palindrome
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int reversed = 0;
        while (x > reversed) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }

        // For even digits, x == reversed
        // For odd digits, x == reversed / 10 (middle digit doesn't matter)
        return (x == reversed || x == reversed / 10);
    }
};