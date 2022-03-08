class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        paliString = list(palindrome)
        for i in range(len(paliString)):
            if palindrome[i] != 'a' and i != (len(palindrome))//2: 
                paliString[i] = 'a'
                break
        else: paliString[len(paliString)-1] = 'b'
        answer = "".join(paliString)
        return answer
