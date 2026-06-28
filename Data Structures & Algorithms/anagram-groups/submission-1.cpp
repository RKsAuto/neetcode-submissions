class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string,vector<string>> result;
        for (const auto& word:strs)
        {
            string alpha(26,0);
            for (const auto& i:word)
            {
                alpha[i-'a'] ++;
            }
            result[alpha].push_back(word);
        }
        vector<vector<string>> ans;
        for(const auto& pair:result)
        {
            ans.push_back(pair.second);
        }
        return ans;
    }
};
