class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        r=[]
        l=[]
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        return sorted(hash, key=hash.get, reverse=True)[:k]