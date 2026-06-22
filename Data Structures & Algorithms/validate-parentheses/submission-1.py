class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in mapping:
                top_element= st.pop() if st else '.'

                if top_element!= mapping[char]:
                    return False
            else:
                st.append(char)
        return not st





        