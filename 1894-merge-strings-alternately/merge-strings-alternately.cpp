class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result; 
        int i=0,j=0;
        int n1 = word1.length(), n2 = word2.length();

        while(i<n1 && j<n2){
            result += word1[i++];
            result += word2[j++];

        }

         if (i < n1) result += word1.substr(i);
         if (j < n2) result += word2.substr(j);

         return result; 

    }
};