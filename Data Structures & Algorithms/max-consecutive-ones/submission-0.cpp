class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count=0, res=0;
        for (int i:nums){
            count= i ? count+1:0;
            res=max(count, res);
        }
    return res;
    }
};