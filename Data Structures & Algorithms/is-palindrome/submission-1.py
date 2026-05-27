class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isdigit():
                result += char
            if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) and not char.isspace():
                result += char.lower()
                
        
        right = len(result) -1
        left = 0
        while(left < right):
            if result[left] == result[right]:
                left +=1
                right -=1
            else:
                return False

        return True