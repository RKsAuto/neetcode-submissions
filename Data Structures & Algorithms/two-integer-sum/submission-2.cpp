#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> comp;
        vector<int> result = {};
        for(int i=0;i<sizeof(nums);i++)
        {
            int compliment = target - nums[i];
            if(comp.find(compliment)!=comp.end())
            {
                result.push_back(comp.find(compliment)->second);
                result.push_back(i);
                return result;
            }
            comp.insert({nums[i],i});
        }
        return result;
    }
};
