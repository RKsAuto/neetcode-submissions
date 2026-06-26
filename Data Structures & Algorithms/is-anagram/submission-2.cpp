#include <vector>
#include <string>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::vector<int> arr(26,0);

        if (s.length()!=t.length())
        {
            return false;
        } 

        for(int i=0;i<s.length();i++)
        {
            arr[s[i] - 'a'] ++;
            arr[t[i] - 'a'] --;
        }

        for(int num:arr)
        {
            if(num!=0)
            {
                return false;
            }
        }
        return true;
    }
};
