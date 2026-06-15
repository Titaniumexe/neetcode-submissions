class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        mp={}
        for i in range(len(s)):
            if s[i] in mp:
                l=max(mp[s[i]]+1, l)
            mp[s[i]]=i
            res=max(res, i-l+1)
        return res


                