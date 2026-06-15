class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        s="".join([c for c in s if c.isalnum()]).lower()
        r=len(s)-1

        while (r>l):
            if s[l]!=s[r]:
                return False
            r-=1
            l+=1
        return True
