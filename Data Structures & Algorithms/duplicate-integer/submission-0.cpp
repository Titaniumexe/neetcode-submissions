class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hash1;
        for (int val:nums){
            if (hash1.count(val)){
                return true;
            }
            hash1.insert(val);
        }
        return false;
    }
};