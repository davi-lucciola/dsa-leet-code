# Time Complexity: O(n²) - "I am not satisfied with the ChatGPT explanation"
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = ''

        for char in s:
            if char.isalnum():
                cleanedStr += char.lower()

        return cleanedStr[::-1] == cleanedStr
