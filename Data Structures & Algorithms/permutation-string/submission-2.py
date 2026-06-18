class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        k=len(s1)
        #Fixed size sliding window

        for i in range(0,len(s2)-k+1):
            print(s2[i:i+k])
            if sorted(s2[i:i+k])==sorted(s1):
                return True
        return False
        