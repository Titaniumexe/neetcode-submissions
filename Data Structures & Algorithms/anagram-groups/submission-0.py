class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        r=[]
        for i in strs:
            key = "".join(sorted(i))
            if key not in hash:
                hash[key]=[i]
            else:
                hash[key].append(i)
        for i in hash:
            r.append(hash[i])
        
        return r