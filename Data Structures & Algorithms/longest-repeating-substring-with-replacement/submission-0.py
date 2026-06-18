class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        maxf=0

        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r], 0)
            maxf= max(maxf, count[s[r]])

            while (r-l+1)- maxf>k:  #If sliding window size- max frequency isnt lesser than k, shorten size of sliding window
                count[s[l]]-=1 #Remove the element in left index to be removed
                l+=1 #Move l index forward
            res= max(res, r-l+1)
        return res






        

        