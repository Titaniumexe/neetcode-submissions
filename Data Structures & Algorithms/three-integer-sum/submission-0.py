class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            numset={}
            for j in range(i+1, n):
                c= -(nums[i]+nums[j])
                if c in numset:
                    res.add((nums[i], nums[j], c))
                numset[nums[j]]=j
        return [list(triplet) for triplet in res]
        